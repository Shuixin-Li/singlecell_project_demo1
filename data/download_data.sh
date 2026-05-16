#!/bin/bash
# ==============================================================================
# Script: download_data.sh
# Description: Automatically download the processed T-cell count matrix for GSE99254
# ==============================================================================

# 如果下载出错，立即停止脚本运行
set -e

echo "=== [Phase 1] Starting Data Download for GSE99254 ==="

# 1. 创建存放原始矩阵的文件夹
mkdir -p raw_matrix

# 2. 使用 wget 从 NCBI FTP 服务器下载处理好的表达矩阵
# -c 参数支持断点续传，-P 指定下载目录
wget -c "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE99nnn/GSE99254/suppl/GSE99254_NSCLC.TCell.S12346.count.txt.gz" -P ./raw_matrix/

echo "=== Download Completed! ==="
echo "=== Unzipping the count matrix ==="

# 3. 解压下载的 .gz 文件
# -f 参数表示如果存在同名解压文件则直接覆盖
gunzip -f ./raw_matrix/GSE99254_NSCLC.TCell.S12346.count.txt.gz

echo "=== All Done! Data is ready at data/raw_matrix/GSE99254_NSCLC.TCell.S12346.count.txt ==="
