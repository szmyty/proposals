from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from mental_health_proposal.visuals import Visualizer


def _text_page(text: str) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8.27, 11.69))
    ax.axis("off")
    ax.text(0.5, 0.5, text, wrap=True, ha="center", va="center", fontsize=12)
    fig.tight_layout()
    return fig


def main() -> None:
    data_path = Path("data/processed/merged.csv")
    df = pd.read_csv(data_path)

    reports_dir = Path("reports")
    images_dir = reports_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    vis = Visualizer()

    scatter_path = images_dir / "depression_vs_obesity.png"
    heatmap_path = images_dir / "correlation_heatmap.png"

    vis.scatter(
        df,
        x="obesity_rate",
        y="depression_rate",
        save_path=scatter_path,
        show=False,
    )
    vis.correlation_heatmap(df, save_path=heatmap_path, show=False)

    correlation = df["depression_rate"].corr(df["obesity_rate"])

    pdf_path = reports_dir / "report.pdf"
    with PdfPages(pdf_path) as pdf:
        intro_text = (
            "Mental Health Data Report\n\n"
            "This report explores simple relationships in the merged dataset. "
            "The scatter plot illustrates the connection between obesity and "
            f"depression rates (correlation {correlation:.2f})."
        )
        pdf.savefig(_text_page(intro_text))
        plt.close()

        scatter_img = plt.imread(scatter_path)
        fig, ax = plt.subplots()
        ax.imshow(scatter_img)
        ax.axis("off")
        ax.set_title("Depression vs Obesity")
        fig.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

        heatmap_img = plt.imread(heatmap_path)
        fig, ax = plt.subplots()
        ax.imshow(heatmap_img)
        ax.axis("off")
        ax.set_title("Correlation Heatmap")
        fig.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

    print(f"Report generated at {pdf_path}")


if __name__ == "__main__":
    main()
