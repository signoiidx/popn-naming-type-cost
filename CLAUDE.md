# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Calculates keystroke counts required to type pop'n music song titles and genres, then compares which is shorter to type. Input data is a CSV of title/genre pairs (not included in the repo — must be downloaded separately from the pastebin in README.md and placed at `data/popn_name_arcade.csv`). Output is written to `data/result.csv`.

## Commands

```bash
# Install dependencies
pip install pykakasi

# Run the analysis
python main.py

# Run tests
pytest

# Run linter
pylint $(git ls-files '*.py')
```

Tests run from the repo root; `tests/test_parse_name.py` adds the parent directory to `sys.path` manually, so no `conftest.py` or `PYTHONPATH` setup is needed.

## Architecture

The pipeline is linear: `main.py` calls three modules in sequence.

- `import_csv.py` — reads the input CSV into a list of `[title, genre]` string pairs
- `parse_name.py` — iterates over pairs, calls `pykakasi.kakasi().convert()` on each string to get Hepburn romanization, concatenates the `hepburn` field from each token, and returns `[title_roman, title_count, genre_roman, genre_count]` per row
- `export_result.py` — writes the result list to `data/result.csv`, creating the `data/` directory if absent

The `data/` directory is gitignored entirely — both input and output files live there and are never committed.

## CI

Two GitHub Actions workflows run on push/PR to `main`:

- **Pytest** — runs `pytest` across Python 3.10–3.13
- **Pylint** — lints all `*.py` files across the same matrix
