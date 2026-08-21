#!/usr/bin/env python3
"""
Scaffold a new topic page from templates/topic-template.md.

Usage:
    python scripts/new_topic.py <folder-under-docs> "<Topic Title>"

Example:
    python scripts/new_topic.py frameworks/langchain "Custom Tools"

This creates docs/frameworks/langchain/custom-tools.md, pre-filled with
the title and a starter tag. It will not overwrite an existing file.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = REPO_ROOT / "templates" / "topic-template.md"
DOCS_ROOT = REPO_ROOT / "docs"


def slugify(title: str) -> str:
    slug = title.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    folder_arg, title = sys.argv[1], sys.argv[2]
    target_dir = DOCS_ROOT / folder_arg
    target_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(title)
    target_file = target_dir / f"{slug}.md"

    if target_file.exists():
        print(f"File already exists: {target_file}")
        sys.exit(1)

    if not TEMPLATE_PATH.exists():
        print(f"Template not found at {TEMPLATE_PATH}")
        sys.exit(1)

    content = TEMPLATE_PATH.read_text(encoding="utf-8")
    content = content.replace("# Topic Title", f"# {title}", 1)
    content = content.replace("  - TODO-add-tags-here", f"  - {title}", 1)

    target_file.write_text(content, encoding="utf-8")

    print(f"Created: {target_file.relative_to(REPO_ROOT)}")
    print("Next: fill in the sections, then git add / commit / push.")


if __name__ == "__main__":
    main()
