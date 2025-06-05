from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class DatasetPaths:
    """Container for dataset file locations."""

    mha: Path
    cdc_places: Path
    samhsa: Path
    kaggle: Path
    modma: Path

    def as_dict(self) -> dict[str, Path]:
        return {
            "mha": self.mha,
            "cdc_places": self.cdc_places,
            "samhsa": self.samhsa,
            "kaggle": self.kaggle,
            "modma": self.modma,
        }


@dataclass
class DataIntegrator:
    paths: DatasetPaths

    def load(self) -> dict[str, pd.DataFrame]:
        """Load all datasets into DataFrames."""
        frames = {}
        for name, path in self.paths.as_dict().items():
            frames[name] = pd.read_csv(path)
        return frames

    def preprocess(self, frames: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
        """Basic preprocessing step to ensure FIPS codes are strings."""
        for df in frames.values():
            if "FIPS" in df.columns:
                df["FIPS"] = df["FIPS"].astype(str)
        return frames

    def merge(self, frames: dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Merge datasets on the FIPS column."""
        merged = frames["mha"]
        for name in ["cdc_places", "samhsa", "kaggle", "modma"]:
            merged = merged.merge(frames[name], on="FIPS", how="outer")
        return merged

    def run(self) -> pd.DataFrame:
        frames = self.load()
        frames = self.preprocess(frames)
        return self.merge(frames)
