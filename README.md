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

## Data Integration

Sample raw data is located in the `data/raw/` directory. These CSV files are
mock representations of the real datasets referenced in the proposal:

- MHA State and County Data
- CDC PLACES
- SAMHSA Data
- Kaggle Mental Health datasets
- MODMA dataset

To merge the datasets for analysis, run:

```bash
python scripts/preprocess_and_merge.py
```

This will create `data/processed/merged.csv`, which can be used for
visualization and further exploration. Replace the sample files in `data/raw/`
with the actual datasets once they have been downloaded.

To generate example visualizations and a PDF report run:

```bash
python scripts/generate_report.py
```

The script will produce images in `reports/images/` and combine them into
`reports/report.pdf`.

## Project Structure

- `src/mental_health_proposal/` – Library code
- `scripts/` – Example scripts
- `data/` – Raw and processed data
- `drafts/` – Original proposal documents
