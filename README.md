# NSCLC T-Cell Landscape Analysis (Reproduction & Optimization)
# 非小细胞肺癌 T 细胞图谱分析 (复现与优化)

[English](#english-version) | [中文版](#中文版)

---

<a name="english-version"></a>
## English Version

### 📖 Introduction
This repository contains a professional reproduction of the landmark single-cell study:  
**"Global characterization of T cells in non-small-cell lung cancer by single-cell sequencing"** (Guo et al., *Nature Medicine* 2018).

This project is divided into two phases: **Faithful Reproduction** of the original findings and **Modern Optimization** using state-of-the-art algorithms.

### 🔬 Project Roadmap

#### Phase 1: Faithful Reproduction (The 2018 Approach)
- **Data:** GSE99254 (Smart-seq2, 12,346 T cells).
- **Methods:** Replicate the original T-cell clusters and exhaustion markers (*LAYN*, *PHLDA1*).
- **Validation:** Compare findings with the original paper's figures (UMAP/Heatmaps).

#### Phase 2: Modern Optimization (The 2026 Approach)
- **Clustering:** Upgrade from hierarchical clustering to **Leiden/Louvain** for better resolution.
- **Integration:** Use **Harmony/scVI** to evaluate batch effect removal performance.
- **Trajectory:** Implement **scVelo** (RNA Velocity) to further investigate T-cell exhaustion dynamics.

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
本项目是对单细胞领域经典研究的专业复现与优化：  
**"Global characterization of T cells in non-small-cell lung cancer by single-cell sequencing"** (Guo et al., *Nature Medicine* 2018)。

本项目分为两个阶段：**经典结果的忠实复现** 以及 **基于前沿算法的现代化优化**。

### 🔬 项目路线图

#### 第一阶段：经典复现 (2018 年方法)
- **数据:** GSE99254 (Smart-seq2 技术, 12,346 个 T 细胞)。
- **方法:** 复现原始 T 细胞分群及耗竭标记基因 (*LAYN*, *PHLDA1*) 的表达特征。
- **验证:** 将分析结果与原论文图表进行比对分析。

#### 第二阶段：现代优化 (2026 年主流方法)
- **聚类优化:** 从传统层级聚类升级为 **Leiden/Louvain 算法**，提升稀有细胞群识别率。
- **整合优化:** 应用 **Harmony/scVI** 评估并优化多患者样本的批次效应处理。
- **轨迹推断:** 引入 **scVelo** (RNA 速率) 等进阶工具，深入探究 T 细胞耗竭的动态演变。

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
