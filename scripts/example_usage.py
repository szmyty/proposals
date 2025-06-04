from mental_health_proposal.pipeline import DataPipeline

if __name__ == "__main__":
    pipeline = DataPipeline()
    # Replace with actual CSV paths
    results = pipeline.run(["data/source1.csv", "data/source2.csv"])
    print(results.head())
