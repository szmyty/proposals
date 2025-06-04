# Mental Health Proposal Prototype

This repository contains a small Python scaffolding to explore the ideas from the proposal located in `drafts/proposal.md`.

## Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install dependencies run:

```bash
poetry install
```

## Usage

The `DataPipeline` class can combine multiple CSV files, run a simple PCA analysis using `scikit-learn`, and provide utilities for generating quick visualizations.

Example usage:

```bash
poetry run python scripts/example_usage.py
```

Replace the paths in `scripts/example_usage.py` with your own data sources.

## Project Structure

- `src/mental_health_proposal/` – Library code
- `scripts/` – Example scripts
- `drafts/` – Original proposal documents
