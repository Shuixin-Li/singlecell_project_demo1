import scanpy as sc

def find_marker_genes(adata, method='wilcoxon'):
    """
    Identify marker genes for each cluster. 
    Methodology follows the standard differential expression testing 
    used in the Kidney Atlas (Lake et al. 2023).
    """
    print(f"Status: Finding marker genes using {method}...")
    
    # Rank genes using the specified statistical test
    sc.tl.rank_genes_groups(adata, 'leiden', method=method)
    
    return adata