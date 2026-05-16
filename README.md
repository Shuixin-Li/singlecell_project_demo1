# Single-Cell RNA-seq Pipeline

This repository implements a production-grade single-cell analysis pipeline.

## 🚀 Getting Started

### 1. Environment Setup
Create the environment using Conda:
```bash
conda env create -f environment.yml
conda activate sc_project
```

### 2. Data Acquisition

This project includes an automated script to fetch the required benchmark dataset. This ensures the pipeline is ready for immediate execution.

Bash

```
python scripts/download_data.py
```

### 3. Execution

Run the end-to-end analysis pipeline (from raw data to visualization):

```bash
python main.py
```

## 📂 Repository Structure

```
.
├── data/               # Raw and processed AnnData objects (Git ignored)
├── results/            # Output directory for analysis results
│   └── figures/        # Automatically generated plots (UMAP, Marker Genes)
├── src/                # Source code
│   ├── preprocess/     # Modules for Quality Control and Normalization
│   ├── analysis/       # Dimensionality reduction and clustering logic
│   └── visualization/  # Custom plotting functions
├── scripts/            # Utility scripts (e.g., Data Download)
├── environment.yml     # Conda environment definition
├── main.py             # Pipeline entry point
└── README.md           # Project documentation
```

## 📈 Key Results

Upon execution, the pipeline generates high-resolution figures in `results/figures/`:

1. **`final_annotated_umap.png`**: The final map showing identified cell populations.
2. **`marker_genes_dotplot.png`**: Statistical ranking of cluster-specific genes, used for biological validation.
3. **`umap_clusters.png`**: Unsupervised clustering before annotation.
