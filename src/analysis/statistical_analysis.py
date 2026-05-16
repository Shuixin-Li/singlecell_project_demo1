import scanpy as sc

def find_marker_genes(adata, method='wilcoxon'):
    """
    Identify marker genes and compute cluster hierarchy.
    """
    print(f"Status: Finding marker genes using {method}...")
    
    # 1. 计算差异表达
    sc.tl.rank_genes_groups(adata, 'leiden', method=method)
    
    # 2. 手动计算树状图，消除 Warning (体现专业性)
    print("Status: Computing cluster dendrogram...")
    sc.tl.dendrogram(adata, groupby='leiden')
    
    return adata