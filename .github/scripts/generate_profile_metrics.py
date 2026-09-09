#!/usr/bin/env python3
"""Generate a dependency-free SVG summary from the public GitHub API."""

from __future__ import annotations

import json
import os
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path


USERNAME = "AminHasanloo"
API_ROOT = "https://api.github.com"


def github_get(path: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AminHasanloo-profile-metrics",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(f"{API_ROOT}{path}", headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def generate_svg(profile: dict, repositories: list[dict]) -> str:
    owned = [repo for repo in repositories if not repo.get("fork")]
    stars = sum(int(repo.get("stargazers_count", 0)) for repo in owned)
    forks = sum(int(repo.get("forks_count", 0)) for repo in owned)
    languages = Counter(repo["language"] for repo in owned if repo.get("language"))
    top_languages = languages.most_common(4)
    language_total = sum(count for _, count in top_languages) or 1
    palette = ["#22D3EE", "#38BDF8", "#818CF8", "#A855F7"]

    stat_values = [
        ("PUBLIC REPOS", profile.get("public_repos", 0)),
        ("TOTAL STARS", stars),
        ("TOTAL FORKS", forks),
        ("FOLLOWERS", profile.get("followers", 0)),
    ]

    cards = []
    for index, (label, value) in enumerate(stat_values):
        x = 34 + index * 284
        cards.append(
            f'<g transform="translate({x} 34)">'
            '<rect width="260" height="98" rx="14" fill="#0B1223" stroke="#24324D"/>'
            f'<text x="22" y="34" class="label">{escape(label)}</text>'
            f'<text x="22" y="75" class="value">{escape(str(value))}</text>'
            f'<rect x="22" y="86" width="68" height="3" rx="1.5" fill="{palette[index]}"/>'
            '</g>'
        )

    bar_width = 790
    bar_x = 34
    bar_parts = []
    legend = []
    cursor = bar_x
    for index, (language, count) in enumerate(top_languages):
        width = bar_width * count / language_total
        bar_parts.append(
            f'<rect x="{cursor:.1f}" y="190" width="{width:.1f}" height="14" fill="{palette[index]}"/>'
        )
        legend_x = bar_x + index * 195
        percentage = round(count * 100 / language_total)
        legend.append(
            f'<circle cx="{legend_x + 6}" cy="234" r="6" fill="{palette[index]}"/>'
            f'<text x="{legend_x + 20}" y="238" class="legend">{escape(language)} {percentage}%</text>'
        )
        cursor += width

    if not top_languages:
        bar_parts.append('<rect x="34" y="190" width="790" height="14" fill="#24324D"/>')
        legend.append('<text x="34" y="238" class="legend">No public language data yet</text>')

    refreshed = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280" role="img" aria-labelledby="title desc">
  <title id="title">Amin Hasanloo public GitHub telemetry</title>
  <desc id="desc">Live counts for public repositories, stars, forks, followers and repository languages.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#070B16"/><stop offset="1" stop-color="#11102A"/></linearGradient>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#7DD3FC" stroke-opacity=".045"/></pattern>
    <style>
      .label{{font:600 12px 'Segoe UI',Arial,sans-serif;letter-spacing:1.8px;fill:#94A3B8}}
      .value{{font:800 34px 'Segoe UI',Arial,sans-serif;fill:#F8FAFC}}
      .legend{{font:600 12px 'Segoe UI',Arial,sans-serif;fill:#CBD5E1}}
      .mono{{font:500 11px Consolas,monospace;letter-spacing:1.3px;fill:#64748B}}
    </style>
    <clipPath id="bar"><rect x="34" y="190" width="790" height="14" rx="7"/></clipPath>
  </defs>
  <rect x="1" y="1" width="1198" height="278" rx="20" fill="url(#bg)" stroke="#20304A" stroke-width="2"/>
  <rect x="1" y="1" width="1198" height="278" rx="20" fill="url(#grid)"/>
  {''.join(cards)}
  <text x="34" y="171" class="label">OWNED PUBLIC REPOSITORIES // PRIMARY LANGUAGE SHARE</text>
  <g clip-path="url(#bar)">{''.join(bar_parts)}</g>
  {''.join(legend)}
  <path d="M862 174h290M862 206h290" stroke="#24324D"/>
  <text x="862" y="193" class="mono">DATA SOURCE  GITHUB API</text>
  <text x="862" y="225" class="mono">REFRESHED    {refreshed} UTC</text>
  <text x="862" y="257" class="mono">SIGNAL       PUBLIC WORK ONLY</text>
</svg>'''


def main() -> None:
    profile = github_get(f"/users/{USERNAME}")
    repositories = github_get(f"/users/{USERNAME}/repos?per_page=100&type=owner")
    output = Path(os.environ.get("OUTPUT_PATH", "dist/profile-metrics.svg"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generate_svg(profile, repositories), encoding="utf-8")
    print(f"Generated {output}")


if __name__ == "__main__":
    main()
