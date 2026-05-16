import scanpy as sc
import pandas as pd

def run_integration(adata, method='harmony'):
    """
    Perform batch correction to integrate multiple samples.
    """
    print(f"Status: Integrating samples using {method}...")
    if method == 'harmony':
        # Ensure you have 'sceasy' or 'harmonypy' installed
        sc.external.pp.harmony_integrate(adata, 'sample_batch')
        adata.obsm['X_pca'] = adata.obsm['X_pca_harmony']
    return adata

def run_trajectory_analysis(adata):
    """
    Compute PAGA to reveal connectivity and transition between cell states.
    """
    print("Status: Computing PAGA trajectory...")
    # 1. Compute neighborhood graph
    sc.pp.neighbors(adata, n_neighbors=15, use_rep='X_pca')
    
    # 2. Run PAGA
    sc.tl.paga(adata, groups='cell_type')
    
    # 3. Re-compute UMAP using PAGA initialization
    sc.tl.umap(adata, init_pos='paga')
    
    return adata