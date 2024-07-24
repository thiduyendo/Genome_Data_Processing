# Genome_Data_Processing
## Project Overview
The Genome Data Processing project is designed to analyze genome data to understand the characteristics of the pan-genome. Specifically, this project aims to determine whether the pan-genome is open or closed by evaluating different genomic metrics. The number of Pan genes, accessory genes, and core genes are calculated by incrementally adding strains into the calculation. The process is iterated 10 times, and average counts are used for analysis.

![Figure 3](https://github.com/user-attachments/assets/c8d2fcf2-293f-4f06-8e2d-72586a11f917)

## Features
- Pan Genes: Genes that are present in at least one genome.
- Core Genes: Genes that are present in all genomes.
- Accessory Genes: Genes that are present in some but not all genomes.
## Installation
To run this project, you need Python and the following packages:
```
pip install pandas numpy h5py
```
## Usage
### Prepare your data: 
Ensure you have your pan-genome data in an HDF5 file format. The file should contain a dataset with the key 'data'.
### Run the script: 
Use the following command to process your data and generate a CSV file with the results:
```
  python pan_genome_count.py --input_file /path/to/your/input_file.h5 --output_file /path/to/your/output_file.csv
```
please use pre_abs.h5 as input_file.h5 and genome_count.csv for the output file
### R Script for Visualization
After generating the genome_data.csv file using the pan_genome_count.py script, you can visualize the data using the provided R script. The R script creates a line plot to illustrate the number of distinct gene clusters (Pan, Core, and Accessory) across different numbers of genomes.
#### Prerequisites
Ensure you have the required R package ggplot2 installed. If not, install it using:
```
install.packages("ggplot2")
```
The R script visualization.R reads the genome_data.csv file and generates a plot.
#### Running the R Script
Execute the visualization.R using your R environment or RStudio. Ensure the file paths in the read.csv and ggsave functions are correctly set to match your directory structure.
```
Rscript visualization.R --input_file /path/to/your/input_file/genome_data.csv --output_file /path/to/your/output_file/genome_plot_test.png
```
## Contact
For any questions or issues, please contact dtduyen1990@gmail.com 
