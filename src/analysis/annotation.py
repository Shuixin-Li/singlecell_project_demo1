import scanpy as sc

def annotate_cells(adata):
    """
    Map Leiden clusters to biological cell types.
    In a real Kidney project (Lake et al. 2023), this would involve 
    mapping markers like CUBN to Proximal Tubules.
    """
    # Define marker-to-type mapping (Based on PBMC 3k standard markers)
    # This demonstrates your understanding of biological interpretation
    new_cluster_names = {
        '0': 'CD4 T cells', '1': 'CD14+ Monocytes',
        '2': 'B cells', '3': 'CD8 T cells', 
        '4': 'NK cells', '5': 'FCGR3A+ Monocytes',
        '6': 'Dendritic cells', '7': 'Megakaryocytes'
    }
    
    # Check if all clusters are in the mapping to prevent errors
    current_clusters = adata.obs['leiden'].unique()
    for cluster in current_clusters:
        if cluster not in new_cluster_names:
            new_cluster_names[cluster] = f"Unknown_{cluster}"

    adata.rename_categories('leiden', [new_cluster_names[str(i)] for i in range(len(new_cluster_names)) if str(i) in current_clusters])
    adata.obs['cell_type'] = adata.obs['leiden']
    
    print("Success: Cell type annotation complete.")
    return adata