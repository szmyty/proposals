from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from mental_health_proposal.integrate import DataIntegrator, DatasetPaths


if __name__ == "__main__":
    base = Path("data/raw")
    paths = DatasetPaths(
        mha=base / "mha_state_county_sample.csv",
        cdc_places=base / "cdc_places_sample.csv",
        samhsa=base / "samhsa_sample.csv",
        kaggle=base / "kaggle_mental_health_sample.csv",
        modma=base / "modma_sample.csv",
    )

    integrator = DataIntegrator(paths)
    merged = integrator.run()
    out_path = Path("data/processed/merged.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(out_path, index=False)
    print(f"Merged data written to {out_path}")
