# NSCLC T-Cell Landscape Analysis (Reproduction)
# 非小细胞肺癌 T 细胞图谱分析 (论文复现)

[English](#english-version) | [中文版](#中文版)

---

<a name="english-version"></a>
## English Version

### 📖 Introduction
This repository contains a professional reproduction of the landmark single-cell study:  
**"Global characterization of T cells in non-small-cell lung cancer by single-cell sequencing"** (Guo et al., *Nature Medicine* 2018).

The project demonstrates a complete single-cell RNA-seq (scRNA-seq) analysis pipeline, transitioning from raw count matrices to biological insights, including T-cell exhaustion states and lineage tracking.

### 🔬 Analysis Roadmap
1. **Data Acquisition (GSE99254):** Retrieve T-cell expression profiles and TCR-seq data.
2. **Standard Processing:** QC filtering (mtRNA < 5%, min_genes > 500), normalization, and log-transformation.
3. **Dimensionality Reduction & Clustering:** PCA followed by UMAP to identify 14+ T-cell clusters (CD8+, CD4+, Treg, etc.).
4. **Exhaustion Analysis:** Characterize the continuum from pre-exhausted to exhausted CD8+ T cells using marker genes like *LAYN*, *PHLDA1*, and *SNAP47*.
5. **Tissue Specificity:** Compare the clonal expansion and migratory patterns between Tumor (T), Adjacent Normal (N), and Peripheral Blood (P).

### 📂 Project Structure
- `data/`: Data scripts and local storage (git-ignored).
- `env/`: Conda environment configuration (`environment.yml`).
- `notebooks/`: Step-by-step Jupyter Notebooks for analysis.
- `scripts/`: Python/R scripts for server-side batch processing.
- `results/`: Key figures and differential expression tables.

---

<a name="中文版"></a>
## 中文版

### 📖 项目简介
本项目是对单细胞领域经典研究的专业复现：  
**"Global characterization of T cells in non-small-cell lung cancer by single-cell sequencing"** (Guo et al., *Nature Medicine* 2018)。

本项目展示了完整的单细胞 RNA 测序 (scRNA-seq) 分析流程：从原始计数矩阵出发，经过严格的质控、降维、聚类，最终揭示 T 细胞耗竭状态及其谱系特征。

### 🔬 分析路线图
1. **数据获取 (GSE99254):** 获取 T 细胞表达谱及 TCR-seq 克隆型数据。
2. **常规处理:** 质控过滤（线粒体基因 < 5%, 检出基因数 > 500）、标准化及对数转换。
3. **降维聚类:** 通过 PCA 和 UMAP 识别出 14 个以上的 T 细胞群（包括 CD8+, CD4+, Treg 等）。
4. **耗竭分析:** 使用 *LAYN*, *PHLDA1* 和 *SNAP47* 等标记基因刻画从“预耗竭”到“耗竭”状态的连续变化。
5. **组织特异性:** 对比肿瘤 (T)、癌旁正常组织 (N) 及外周血 (P) 中 T 细胞的克隆扩增与迁移模式。

### 📂 目录架构
- `data/`: 数据下载脚本及本地存储（已设 git-ignore）。
- `env/`: Conda 环境配置文件 (`environment.yml`)。
- `notebooks/`: 循序渐进的分析过程记录 (Jupyter)。
- `scripts/`: 用于服务器批量运行的脚本。
- `results/`: 关键分析图表及差异表达基因列表。

---

## 🚀 Quick Start / 快速开始

1. **Clone the repo / 克隆仓库:**
   ```bash
   git clone [https://github.com/Shuixin-Li/singlecell_project.git](https://github.com/Shuixin-Li/singlecell_project.git)
   cd singlecell_project
