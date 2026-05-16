import scanpy as sc
import os

def prepare_data():
    """
    Downloads the PBMC 3k dataset as a benchmark for the pipeline.
    """
    raw_dir = "data/raw"
    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)
    
    raw_path = os.path.join(raw_dir, "pbmc_raw.h5ad")
    
    if not os.path.exists(raw_path):
        print("Status: Downloading PBMC 3k benchmark dataset...")
        # This function fetches 5.9MB of data from 10X Genomics
        adata = sc.datasets.pbmc3k()
        adata.write(raw_path)
        print(f"Success: Data saved to {raw_path}")
    else:
        print(f"Info: Data file {raw_path} already exists. Skipping download.")

if __name__ == "__main__":
    prepare_data()