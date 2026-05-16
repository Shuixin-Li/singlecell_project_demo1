import scanpy as sc
import numpy as np

def estimate_cell_communication(adata):
    """
    Simplified cell-cell communication based on cluster-specific expression.
    Shows the interaction strength between different cell types.
    """
    print("Status: Estimating cell-cell communication scores...")
    # This is a proxy: calculating mean expression of key signaling genes per cluster
    # Example: TGFB1 (Ligand) -> TGFBR1 (Receptor)
    signaling_genes = ['TGFB1', 'TGFBR1', 'CCL5', 'CCR5']
    
    # Check which genes are in the dataset
    valid_genes = [g for g in signaling_genes if g in adata.var_names]
    
    if valid_genes:
        communication_df = pd.DataFrame(
            index=adata.obs['cell_type'].cat.categories,
            columns=valid_genes
        )
        for gene in valid_genes:
            # Mean expression per cluster
            communication_df[gene] = adata[:, gene].X.mean(axis=0)
            
        print("Success: Communication proxy calculated.")
        return communication_df
    return None