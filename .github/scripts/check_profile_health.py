#!/usr/bin/env python3
"""Verify local profile assets and public README links using only Python stdlib."""

from __future__ import annotations

import os
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
USER_AGENT = "AminHasanloo-profile-health/1.0"
ATTRIBUTE_PATTERN = re.compile(r'(?:href|src|srcset)="([^"]+)"')
MARKDOWN_PATTERN = re.compile(r'\]\((https://[^)\s]+)\)')
IGNORED_REMOTE_HOSTS = {"www.linkedin.com"}  # Returns anti-bot status 999 to automated checks.


def extract_targets(markdown: str) -> tuple[list[str], list[str]]:
    attribute_values = [value.replace("&amp;", "&").split()[0] for value in ATTRIBUTE_PATTERN.findall(markdown)]
    markdown_urls = [value.replace("&amp;", "&") for value in MARKDOWN_PATTERN.findall(markdown)]
    values = sorted(set(attribute_values + markdown_urls))
    remote = [
        value
        for value in values
        if value.startswith("https://") and urlparse(value).netloc not in IGNORED_REMOTE_HOSTS
    ]
    local = [value for value in values if not value.startswith(("http://", "https://", "mailto:"))]
    return remote, local


def request_url(url: str) -> tuple[str, bool, str]:
    last_error = "unknown error"
    for attempt in range(2):
        for method in ("HEAD", "GET"):
            try:
                request = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(request, timeout=25) as response:
                    status = int(response.status)
                    if 200 <= status < 400:
                        return url, True, str(status)
                    last_error = f"HTTP {status}"
            except urllib.error.HTTPError as error:
                last_error = f"HTTP {error.code}"
            except Exception as error:  # Network errors need useful context in Actions logs.
                last_error = f"{type(error).__name__}: {error}"
        if attempt == 0:
            time.sleep(1)
    return url, False, last_error


def append_summary(lines: list[str]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("\n".join(lines) + "\n")


def main() -> None:
    markdown = README.read_text(encoding="utf-8")
    remote_urls, local_paths = extract_targets(markdown)

    missing_local = [path for path in local_paths if not (ROOT / path).is_file()]
    with ThreadPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(request_url, remote_urls))
    broken_remote = [(url, detail) for url, ok, detail in results if not ok]

    lines = [
        "## Profile health",
        "",
        f"- Local assets checked: {len(local_paths)}",
        f"- Public URLs checked: {len(remote_urls)}",
        f"- Missing local assets: {len(missing_local)}",
        f"- Broken public URLs: {len(broken_remote)}",
    ]

    if missing_local:
        lines.extend(["", "### Missing local assets", *[f"- `{path}`" for path in missing_local]])
    if broken_remote:
        lines.extend(["", "### Broken public URLs", *[f"- {url} — {detail}" for url, detail in broken_remote]])

    append_summary(lines)
    print("\n".join(lines))

    if missing_local or broken_remote:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
