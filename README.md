
# Single-Cell RNA-seq Engineering Demo

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Scanpy](https://img.shields.io/badge/library-Scanpy-brightgreen.svg)](https://scanpy.readthedocs.io/)

A modular, production-ready pipeline for single-cell RNA-seq analysis. This project demonstrates best practices in bioinformatics software engineering, featuring a config-driven architecture, automated quality control, and advanced downstream analysis.

---

## 🌟 Core Functionalities

- **Modular Design**: Code is organized into functional modules for high maintainability.
- **Config-Driven**: Analysis parameters are managed via `YAML` files to ensure full reproducibility.
- **End-to-End Workflow**:
  - Automated data acquisition.
  - Standardized QC (Mitochondrial & Gene filtering).
  - Dimensionality reduction (PCA) and manifold learning (UMAP).
  - Graph-based clustering (Leiden) and cluster hierarchy (Dendrogram).
  - **Advanced**: Trajectory inference (PAGA) and Cell-cell communication proxy.

---

## 📂 Repository Structure

```text
.
├── data/               # Local data storage (Git ignored)
│   ├── raw/            # Raw .h5ad files
│   └── processed/      # Analysis results (.h5ad & .csv)
├── results/            # Pipeline outputs
│   └── figures/        # Generated UMAPs, PAGA, and Dotplots
├── src/                # Source Code
│   ├── config/         # YAML configuration files
│   ├── preprocess/     # Data cleaning and normalization
│   └── analysis/       # Clustering, Trajectory, and Annotation
├── scripts/            # Utility scripts (Data download, etc.)
├── main.py             # Pipeline entry point
├── environment.yml     # Conda environment definition
└── README.md           # Documentation
```

------

## 🚀 Getting Started

### 1. Environment Setup

Create and activate the environment using the provided YAML file:

```bash
conda env create -f environment.yml
conda activate sc_project
```

### 2. Execution

Run the following commands in sequence:

```bash
# Fetch the benchmark dataset
python scripts/download_data.py

# Execute the full analysis pipeline
python main.py
```

------

## 📊 Key Analysis Results

The pipeline automatically generates high-quality visualizations in `results/figures/`:

##### 1. Cell Population Identification

Dimensionality reduction via UMAP with automated cell type annotation.

##### 2. Lineage & Trajectory Analysis

PAGA-based graph abstraction revealing the connectivity and transition paths between cell clusters.

##### 3. Marker Gene Expression

Dotplot visualization of top-ranked genes defining each cluster, including hierarchical relationship analysis.

------

## ⚙️ Configuration

This project utilizes a `src/config/config.yaml` file to manage all hyperparameters. This allows users to adjust QC thresholds (e.g., `max_mito`), clustering resolution, and file paths without modifying the core source code.
