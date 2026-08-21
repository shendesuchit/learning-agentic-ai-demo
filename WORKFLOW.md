# How to Add a New Topic — Workflow Guide

This is the entire process for adding new learning content to the site.
No `mkdocs.yml` edits required for day-to-day content — navigation is
generated automatically from the folder structure.

---

## Step 1 — Copy the template

Duplicate `templates/topic-template.md` into the right folder under `docs/`.
Choose the folder based on where the topic fits your learning hierarchy —
that folder placement is now the *only* navigation decision you make.

```bash
cp templates/topic-template.md docs/frameworks/langchain/new-topic.md
```

---

## Step 2 — Fill in the sections

Work through the template in order:

1. Concept
2. Why It Matters
3. Mental Model
4. Diagram
5. Example
6. My Understanding
7. Common Mistakes
8. Related Topics
9. References
10. Implementation

Add relevant tags in the frontmatter block at the top of the file, e.g.:

```yaml
---
tags:
  - LangChain
  - Middleware
  - Beginner
---
```

---

## Step 3 — Skip `mkdocs.yml` entirely

You do not need to touch `mkdocs.yml` or any nav list for a new page.
The `awesome-pages` plugin discovers the new file automatically from the
folder structure the next time the site builds.

---

## Step 4 — (Optional) Set order within a folder

If you care about the exact order pages appear in within a specific folder,
add or edit a `.pages` file in that folder:

```yaml
nav:
  - introduction.md
  - new-topic.md
```

If you don't add one, MkDocs falls back to alphabetical order — usually
fine, so skip this step most of the time.

---

## Step 5 — Commit and push

```bash
git add .
git commit -m "docs: add topic on <name>"
git push origin main
```

That's the entire authoring loop from here on.

---

## Step 6 — Netlify rebuilds automatically

Nav, search index, and the tags index page (`/tags/`) all update themselves.
Open the live URL and confirm:

- The new page appears under the right tab.
- The tags you added show up on the Tags page.

---

## Quick reference

| I want to... | Do this |
|---|---|
| Add a new topic page | Copy `templates/topic-template.md` into the right `docs/` folder, fill it in, push |
| Reorder pages in a folder | Add/edit a `.pages` file in that folder |
| Add a brand-new top-level section (rare) | Create the folder under `docs/`, add it to `docs/.pages` |
| Change site-wide theme/colors/plugins | Edit `mkdocs.yml` (not needed for normal content work) |
