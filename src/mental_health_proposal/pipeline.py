from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import pandas as pd

from .ingest import DataIngestor
from .analysis import PCAAnalyzer

@dataclass
class DataPipeline:
    ingestor: DataIngestor = field(default_factory=DataIngestor)
    analyzer: PCAAnalyzer = field(default_factory=PCAAnalyzer)

    def run(self, csv_files: list[str]) -> pd.DataFrame:
        frames = [self.ingestor.load_csv(Path(f)) for f in csv_files]
        combined = pd.concat(frames, ignore_index=True)
        return self.analyzer.fit_transform(combined)
