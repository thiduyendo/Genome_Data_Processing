# Genome_Data_Processing
## Project Overview
The Genome Data Processing project is designed to analyze genome data to understand the characteristics of the pan-genome. Specifically, this project aims to determine whether the pan-genome is open or closed by evaluating different genomic metrics. The number of Pan genes, accessory genes, and core genes are calculated by incrementally adding strains into the calculation. The process is iterated 10 times, and average counts are used for analysis.
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
- Prepare your data: Ensure you have your pan-genome data in an HDF5 file format. The file should contain a dataset with the key 'data'.
- Run the script: Use the following command to process your data and generate a CSV file with the results:
```
  python pan_genome_count.py --input_file /path/to/your/input_file.h5 --output_file /path/to/your/output_file.csv
```
## Contact
For any questions or issues, please contact dtduyen1990@gmail.com 
