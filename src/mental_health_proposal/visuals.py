import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    """Utility class for generating common visualizations."""

    def scatter(self, df: pd.DataFrame, x: str, y: str, hue: str | None = None) -> None:
        sns.scatterplot(data=df, x=x, y=y, hue=hue)
        plt.show()

    def correlation_heatmap(self, df: pd.DataFrame) -> None:
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.show()
