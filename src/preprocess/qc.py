import scanpy as sc
import os

def run_pipeline_qc(adata, min_genes=200, min_cells=3, max_mito=5):
    """
    Quality Control and Normalization
    """
    print(f"Status: Starting QC with {adata.n_obs} cells...")

    # 1. Calculate QC metrics (Mitochondrial genes)
    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

    # 2. Filtering
    # Note: For kidney tissue, the paper used a 20% mito threshold.
    # Here for PBMC, we use 5% to maintain biological accuracy for blood cells.
    sc.pp.filter_cells(adata, min_genes=min_genes)
    sc.pp.filter_genes(adata, min_cells=min_cells)
    adata = adata[adata.obs.pct_counts_mt < max_mito, :].copy()

    # 3. Normalization and Log transformation
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

    # 4. Identify Highly Variable Genes (HVGs)
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
    
    print(f"Success: QC complete. Remaining cells: {adata.n_obs}")
    return adata
