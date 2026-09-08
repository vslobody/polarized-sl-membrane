# GitHub Setup Checklist

## Repository name

Recommended: `polarized-sl-membrane-cosmology`

## Initial files

Upload this package as the initial repository content.

Required:

- `README.md`
- `docs/one_page_summary.md`
- `docs/landing_page.md`
- `papers/`
- `notes/`
- `figures/`
- `calculations/`
- `posts/`
- `outreach/`
- `references.bib`
- `CITATION.cff`

## GitHub Pages

Use GitHub Pages to create a single public front door. Simplest path:

1. Create public repo.
2. Put landing content in `/docs`.
3. In repo settings, enable Pages from the main branch `/docs` folder.
4. Use `docs/landing_page.md` as the initial landing page content, or rename it to `index.md`.

## Citation

Keep `CITATION.cff` in the repository root. GitHub uses citation files to display a citation prompt for the repository.

## Zenodo

After the repository is stable, connect it to Zenodo and archive a release. Zenodo can archive GitHub releases and issue a DOI. Keep DOI metadata synchronized with `.zenodo.json` if you decide to add it later.

## First release

Suggested tag: `v0.1-front-door`

Suggested release title:

`Front-door package for Polarized Sl-Membrane Cosmology`

Release notes:

- Adds one-page entry note.
- Adds Opus I--III PDFs and Conjecture I.
- Adds overview diagram.
- Adds hostile-review request.
- Adds initial relic-statistics sanity check script.
