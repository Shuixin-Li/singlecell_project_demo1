import scanpy as sc

def find_marker_genes(adata, method='wilcoxon'):
    """
    Identify marker genes and compute cluster hierarchy.
    """
    print(f"Status: Finding marker genes using {method}...")
    
    sc.tl.rank_genes_groups(adata, 'leiden', method=method)
    
    print("Status: Computing cluster dendrogram...")
    sc.tl.dendrogram(adata, groupby='leiden')
    
    return adata