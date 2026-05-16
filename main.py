import scanpy as sc
import os
import matplotlib.pyplot as plt
from src.preprocess.qc import run_pipeline_qc
from src.analysis.statistical_analysis import find_marker_genes

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

    # 4. Dimensionality Reduction
    print("Step 3: Running PCA and UMAP...")
    sc.tl.pca(adata, svd_solver='arpack')
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
    sc.tl.umap(adata)

    # 5. Clustering
    print("Step 4: Clustering cells...")
    sc.tl.leiden(adata)

    # 6. Marker Gene Analysis
    print("Step 5: Identifying marker genes...")
    adata = find_marker_genes(adata)

    # 7. Visualization
    print(f"Step 6: Saving final visualizations to {output_dir}...")
    
    # Save UMAP
    sc.pl.umap(adata, color=['leiden'], show=False)
    plt.savefig(os.path.join(output_dir, "umap_clusters.png"), bbox_inches='tight')
    plt.close()

    # Save Marker Gene Dotplot (Highly professional viz)
    sc.pl.rank_genes_groups_dotplot(adata, n_genes=3, show=False)
    plt.savefig(os.path.join(output_dir, "marker_genes_dotplot.png"), bbox_inches='tight')
    plt.close()

    # 8. Save Processed Object
    adata.write("data/processed/pbmc_processed.h5ad")
    print("\nAll steps completed! Check results/figures/ for outputs.")

if __name__ == "__main__":
    main()