# Dhyey's Learning Lab — Demo

A small proof-of-concept learning documentation site built with MkDocs Material.

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve
```

Open the local URL shown by MkDocs.

## Netlify

This repository is configured for Netlify continuous deployment.

- Build command: `mkdocs build`
- Publish directory: `site`

See `netlify.toml` for the configuration.
