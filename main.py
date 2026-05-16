import os
import yaml
import scanpy as sc
import matplotlib.pyplot as plt
import logging

# Import custom modules
from src.preprocess.qc import run_pipeline_qc
from src.analysis.statistical_analysis import find_marker_genes
from src.analysis.annotation import annotate_cells
from src.analysis.advanced_analysis import run_trajectory_analysis
from src.analysis.communication import estimate_cell_communication

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    # ---------------------------------------------------------
    # 1. Configuration & Path Setup
    # ---------------------------------------------------------
    config_path = "src/config/config.yaml"
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    raw_path = config['paths']['raw_data']
    output_dir = config['paths']['figures']
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    logger.info(f"Starting {config['project_name']} pipeline...")

    # ---------------------------------------------------------
    # 2. Data Loading & Preprocessing
    # ---------------------------------------------------------
    logger.info("Step 1: Loading raw AnnData...")
    adata = sc.read_h5ad(raw_path)
    
    # Simulate a batch column for the demo (normally exists in raw data)
    if 'sample_batch' not in adata.obs.columns:
        adata.obs['sample_batch'] = 'Batch_1'

    logger.info("Step 2: Running Quality Control...")
    adata = run_pipeline_qc(
        adata, 
        min_genes=config['qc_params']['min_genes'], 
        max_mito=config['qc_params']['max_mito']
    )

    # ---------------------------------------------------------
    # 3. Standard Analysis (Dimensionality Reduction & Clustering)
    # ---------------------------------------------------------
    logger.info("Step 3: Dimensionality reduction (PCA/UMAP)...")
    sc.tl.pca(adata, svd_solver='arpack')
    
    # Optional: Integration (Batch Correction)
    # adata = run_integration(adata, method=config['analysis_params']['integration_method'])
    
    sc.pp.neighbors(adata, n_neighbors=config['analysis_params']['n_neighbors'], n_pcs=config['analysis_params']['n_pcs'])
    sc.tl.umap(adata)

    logger.info("Step 4: Clustering & Statistical Analysis...")
    sc.tl.leiden(adata, resolution=config['analysis_params']['resolution'])
    adata = find_marker_genes(adata)

    # ---------------------------------------------------------
    # 4. Biological Interpretation (Annotation)
    # ---------------------------------------------------------
    logger.info("Step 5: Mapping cell type annotations...")
    adata = annotate_cells(adata)

    # ---------------------------------------------------------
    # 5. Advanced Analysis (Trajectory & Communication)
    # ---------------------------------------------------------
    logger.info("Step 6: Running Advanced Trajectory Analysis (PAGA)...")
    adata = run_trajectory_analysis(adata)
    
    # Save PAGA Plot
    sc.pl.paga(adata, show=False)
    plt.savefig(os.path.join(output_dir, "trajectory_paga.png"), bbox_inches='tight')
    plt.close()

    logger.info("Step 7: Estimating Cell-Cell Communication...")
    comm_df = estimate_cell_communication(adata)
    if comm_df is not None:
        comm_df.to_csv("data/processed/communication_matrix.csv")
        logger.info("Communication matrix saved to data/processed/")

    # ---------------------------------------------------------
    # 6. Final Visualization & Export
    # ---------------------------------------------------------
    logger.info("Step 8: Exporting final visualizations...")
    
    # Final Annotated UMAP
    sc.pl.umap(adata, color='cell_type', legend_loc='on data', frameon=False, show=False)
    plt.savefig(os.path.join(output_dir, "final_annotated_umap.png"), bbox_inches='tight')
    plt.close()

    # Marker Gene Dotplot
    sc.pl.rank_genes_groups_dotplot(adata, n_genes=3, show=False)
    plt.savefig(os.path.join(output_dir, "marker_genes_dotplot.png"), bbox_inches='tight')
    plt.close()

    # Save the Final AnnData Object
    adata.write(config['paths']['processed_data'])
    logger.info(f"Pipeline finished! Processed data saved to {config['paths']['processed_data']}")

if __name__ == "__main__":
    main()