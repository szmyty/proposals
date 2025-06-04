from __future__ import annotations

from dataclasses import dataclass
import pandas as pd
from sklearn.decomposition import PCA

@dataclass
class PCAAnalyzer:
    n_components: int = 2

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pca = PCA(n_components=self.n_components)
        components = pca.fit_transform(df.select_dtypes(include='number'))
        columns = [f'PC{i+1}' for i in range(self.n_components)]
        return pd.DataFrame(components, columns=columns)
