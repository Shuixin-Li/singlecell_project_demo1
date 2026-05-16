import scanpy as sc
import os
import matplotlib.pyplot as plt
from src.preprocess.qc import run_pipeline_qc
from src.analysis.statistical_analysis import find_marker_genes
from src.analysis.annotation import annotate_cells

def main():
    # 1. Setup
    input_path = "data/raw/pbmc_raw.h5ad"
    output_dir = "results/figures"
    os.makedirs(output_dir, exist_ok=True)

    # 2. Load & Preprocess
    adata = sc.read_h5ad(input_path)
    adata = run_pipeline_qc(adata)

    # 3. Dimensionality Reduction
    sc.tl.pca(adata)
    sc.pp.neighbors(adata)
    sc.tl.umap(adata)

    # 4. Clustering & Stats
    sc.tl.leiden(adata)
    adata = find_marker_genes(adata)

    # 5. Annotation (The "Soul" of the project)
    adata = annotate_cells(adata)

    # 6. Final Visualization
    print("Step 6: Generating final annotated UMAP...")
    sc.pl.umap(adata, color='cell_type', legend_loc='on data', show=False)
    plt.savefig(os.path.join(output_dir, "final_annotated_umap.png"), bbox_inches='tight')
    plt.close()

    # 7. Save result
    adata.write("data/processed/pbmc_final.h5ad")
    print("\n--- Project Fully Executed! ---")

if __name__ == "__main__":
    main()