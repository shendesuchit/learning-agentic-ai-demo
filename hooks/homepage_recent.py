"""
Auto-populates the "Recent Learning" section on the homepage.

Scans docs/ for the most recently git-modified Markdown pages (excluding
index.md and tags.md), pulls a title and short summary out of each, and
renders them as a Material grid-cards block wherever the marker

    <!-- AUTO:RECENT_LEARNING -->

appears in docs/index.md. Requires full git history to be available at
build time (fetch-depth 0 / an unshallowed clone) — see WORKFLOW.md.
"""

import subprocess
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
MARKER = "<!-- AUTO:RECENT_LEARNING -->"
COUNT = 3
EXCLUDE = {"index.md", "tags.md"}

# Cycled through in order so cards get some visual variety without
# needing per-page icon configuration.
ICONS = [
    "material-tune-vertical",
    "material-code-braces",
    "material-graph-outline",
    "material-file-document-outline",
    "material-book-open-page-variant-outline",
]


def _git_last_modified(path: Path) -> int:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(path)],
            cwd=path.parent,
            capture_output=True,
            text=True,
            check=True,
        )
        ts = result.stdout.strip()
        return int(ts) if ts else 0
    except Exception:
        return 0


def _extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _extract_summary(md_text: str) -> str:
    lines = [l.strip() for l in md_text.splitlines()]
    for i, line in enumerate(lines):
        if line.startswith("## ") and "concept" in line.lower():
            for candidate in lines[i + 1 :]:
                if candidate and not candidate.startswith("#"):
                    return candidate
    return "Recently updated."


def _build_cards() -> str:
    md_files = [p for p in DOCS_DIR.rglob("*.md") if p.name not in EXCLUDE]
    dated = [(p, _git_last_modified(p)) for p in md_files]
    dated = [d for d in dated if d[1] > 0]
    dated.sort(key=lambda x: x[1], reverse=True)
    recent = dated[:COUNT]

    if not recent:
        return "*No topic pages yet — add one to see it here automatically.*"

    cards = ['<div class="grid cards" markdown>\n']
    for i, (path, _) in enumerate(recent):
        text = path.read_text(encoding="utf-8")
        title = _extract_title(text, path.stem.replace("-", " ").title())
        summary = _extract_summary(text)
        rel_link = path.relative_to(DOCS_DIR).as_posix()
        icon = ICONS[i % len(ICONS)]
        cards.append(
            f"-   :{icon}:{{ .lg .middle }} **{title}**\n\n"
            f"    ---\n\n"
            f"    {summary}\n\n"
            f"    [:octicons-arrow-right-24: Read {title}]({rel_link})\n"
        )
    cards.append("</div>")
    return "\n".join(cards)


def on_page_markdown(markdown, page, config, files):
    if page.file.src_path.replace("\\", "/") != "index.md":
        return markdown
    if MARKER not in markdown:
        return markdown
    return markdown.replace(MARKER, _build_cards())
