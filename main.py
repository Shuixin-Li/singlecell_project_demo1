import scanpy as sc
import os
from src.preprocess.qc import run_pipeline_qc

def main():
    # 1. Setup paths
    input_path = "data/raw/pbmc_raw.h5ad"
    output_dir = "results/figures"
    os.makedirs(output_dir, exist_ok=True)

    # 2. Load Data
    print("Step 1: Loading data...")
    adata = sc.read_h5ad(input_path)

    # 3. Preprocessing (QC)
    print("Step 2: Preprocessing...")
    adata = run_pipeline_qc(adata)

    # 4. Analysis: PCA, Neighbors, and UMAP
    print("Step 3: Running dimensionality reduction...")
    sc.tl.pca(adata, svd_solver='arpack')
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
    sc.tl.umap(adata)

    # 5. Clustering
    print("Step 4: Clustering cells using Leiden algorithm...")
    sc.tl.leiden(adata)

    # 6. Visualization & Saving
    print(f"Step 5: Saving visualization to {output_dir}...")
    
    # Save UMAP plot
    sc.pl.umap(adata, color=['leiden'], show=False)
    import matplotlib.pyplot as plt
    plt.savefig(os.path.join(output_dir, "umap_clusters.png"), bbox_inches='tight')
    
    # Save the processed data
    adata.write("data/processed/pbmc_processed.h5ad")
    print("\nPipeline execution finished successfully!")

if __name__ == "__main__":
    main()