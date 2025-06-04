from pathlib import Path
import pandas as pd

class DataIngestor:
    """Basic data ingestion utilities."""

    def load_csv(self, path: Path) -> pd.DataFrame:
        """Load a CSV file into a DataFrame."""
        return pd.read_csv(path)

    def load_json(self, path: Path) -> pd.DataFrame:
        """Load a JSON file into a DataFrame."""
        return pd.read_json(path)
