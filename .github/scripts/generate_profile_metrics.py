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
    palette = ["#22D3EE", "#60A5FA", "#A78BFA", "#FACC15"]

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
            '<rect x="7" y="7" width="260" height="98" fill="#030712"/>'
            '<rect width="260" height="98" fill="#0B1223" stroke="#334155" stroke-width="3"/>'
            f'<text x="22" y="34" class="label">{escape(label)}</text>'
            f'<text x="22" y="75" class="value">{escape(str(value))}</text>'
            f'<rect x="22" y="86" width="68" height="5" fill="{palette[index]}"/>'
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
            f'<rect x="{legend_x}" y="228" width="12" height="12" fill="{palette[index]}"/>'
            f'<text x="{legend_x + 20}" y="238" class="legend">{escape(language)} {percentage}%</text>'
        )
        cursor += width

    if not top_languages:
        bar_parts.append('<rect x="34" y="190" width="790" height="14" fill="#24324D"/>')
        legend.append('<text x="34" y="238" class="legend">No public language data yet</text>')

    refreshed = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280" role="img" aria-labelledby="title desc" shape-rendering="crispEdges">
  <title id="title">Amin Hasanloo public GitHub telemetry</title>
  <desc id="desc">Live counts for public repositories, stars, forks, followers and repository languages.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#070B16"/><stop offset="1" stop-color="#11102A"/></linearGradient>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#7DD3FC" stroke-opacity=".045"/></pattern>
    <style>
      .label{{font:700 12px 'Courier New',Consolas,monospace;letter-spacing:1.8px;fill:#94A3B8}}
      .value{{font:900 34px 'Courier New',Consolas,monospace;fill:#F8FAFC}}
      .legend{{font:700 12px 'Courier New',Consolas,monospace;fill:#CBD5E1}}
      .mono{{font:700 11px 'Courier New',Consolas,monospace;letter-spacing:1.3px;fill:#64748B}}
    </style>
    <clipPath id="bar"><rect x="34" y="190" width="790" height="14"/></clipPath>
  </defs>
  <rect x="1" y="1" width="1198" height="278" fill="url(#bg)" stroke="#22D3EE" stroke-width="3"/>
  <rect x="1" y="1" width="1198" height="278" fill="url(#grid)"/>
  <path d="M2 24h22V2M1176 2v22h22M2 256h22v22M1176 278v-22h22" fill="none" stroke="#FACC15" stroke-width="4"/>
  {''.join(cards)}
  <text x="34" y="171" class="label">OWNED PUBLIC REPOSITORIES // PRIMARY LANGUAGE SHARE</text>
  <g clip-path="url(#bar)">{''.join(bar_parts)}</g>
  {''.join(legend)}
  <path d="M862 174h290M862 206h290" stroke="#24324D"/>
  <rect x="1138" y="181" width="10" height="10" fill="#4ADE80"/>
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
