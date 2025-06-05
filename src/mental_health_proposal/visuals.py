import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    """Utility class for generating common visualizations."""

    def scatter(
        self,
        df: pd.DataFrame,
        x: str,
        y: str,
        hue: str | None = None,
        save_path: str | None = None,
        show: bool = True,
    ) -> plt.Figure:
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x, y=y, hue=hue, ax=ax)
        fig.tight_layout()
        if save_path:
            fig.savefig(save_path)
        if show:
            plt.show()
        else:
            plt.close(fig)
        return fig

    def correlation_heatmap(
        self,
        df: pd.DataFrame,
        save_path: str | None = None,
        show: bool = True,
    ) -> plt.Figure:
        fig, ax = plt.subplots()
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        fig.tight_layout()
        if save_path:
            fig.savefig(save_path)
        if show:
            plt.show()
        else:
            plt.close(fig)
        return fig
