# disnake-era-template

Powerful [kickstart](https://github.com/Keats/kickstart) template for new
disnake extension projects.

## Components

- Python 3.8+ end-user, 3.9+ developer.
- Project management using [PDM](https://pdm.fming.dev/).
- Linting and formatting using [ruff](https://github.com/astral-sh/ruff).
- Strict type checking using [pyright](https://github.com/microsoft/pyright).
- Documentation using [Sphinx](https://github.com/sphinx-doc/Sphinx).
- - `sphinx-rtd-theme` theme.
- - Fragments-based changelogs using [Towncrier](https://github.com/twisted/towncrier) and `sphinxcontrib-towncrier`.
- - Support for [ReadTheDocs](https://readthedocs.org/).
- [pre-commit](https://pre-commit.com/) hooks.
- GitHub Actions workflows (build, lint, format, docs, type-check).
- Automatic dependency updates via dependabot.

## Usage

Install kickstart, then run

```sh
kickstart https://github.com/disnake-era/template
```

And input values. After the project is generated, run `git init`, create a LICENSE with appropriate contents
and you're good to go!
