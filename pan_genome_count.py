import pandas as pd
import numpy as np
import h5py, csv, argparse


def process_genome_data(input_file, output_file):
	print(f"Loading data from {input_file}...")
	df = pd.read_hdf(input_file, key='data')
	df0 = df.astype(int)
	print('Printing Pan-genome table: ', df0)

	num_genome = {}
	avg_num_genome = {}
	final = {}

	# Process each increment of the genome
	for i in range(1, df.shape[0] + 1):
		num_genome[i] = {}
		avg_num_genome[i] = {'pan': [], 'core': [], 'accessory': []}
		final[i] = {'pan': [], 'core': [], 'accessory': []}

	# Shuffle and process the data 10 times
	print("Shuffling and processing data 10 times...")
	for _ in range(10):
		df_shuffled = df.sample(frac=1)
		for i in range(1, df_shuffled.shape[0] + 1):
			current_table = df_shuffled.iloc[:i]
			col_sums = current_table.sum()
			
			# Filter columns based on criteria
			pan = col_sums[col_sums >= 1]
			core = col_sums[col_sums == current_table.shape[0]]
			accessory = col_sums[(col_sums >= 1) & (col_sums < current_table.shape[0])]
			
			# Count the number of rows (unitigs) meeting the criteria
			num_genome[i]['pan'] = len(pan)
			num_genome[i]['core'] = len(core)
			num_genome[i]['accessory'] = len(accessory)
			avg_num_genome[i]['pan'].append(len(pan))
			avg_num_genome[i]['core'].append(len(core))
			avg_num_genome[i]['accessory'].append(len(accessory))

	# Calculate the average number of unitigs for each incremental addition of a genome
	print("Calculating average number of unitigs...")
	for i in range(1, df_shuffled.shape[0] + 1):
		final[i]['pan'] = sum(avg_num_genome[i]['pan']) / len(avg_num_genome[i]['pan'])
		final[i]['core'] = sum(avg_num_genome[i]['core']) / len(avg_num_genome[i]['core'])
		final[i]['accessory'] = sum(avg_num_genome[i]['accessory']) / len(avg_num_genome[i]['accessory'])

	# Create a new file called "genome_data.csv" in write mode
	print(f"Saving results to {output_file}...")
	with open(output_file, 'w', newline='') as file: 
		# Create a CSV writer object
		writer = csv.writer(file)
		# Write the header row
		writer.writerow(['Genome', 'Pan', 'Core', 'Accessory'])
		# Write the data rows
		for genome, values in final.items():
			writer.writerow([genome, values['pan'], values['core'], values['accessory']])

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process genome data.')
	parser.add_argument('--input_file', type=str, required=True, help='Path to the input HDF5 file')
	parser.add_argument('--output_file', type=str, required=True, help='Path to the output CSV file')
	args = parser.parse_args()
	process_genome_data(args.input_file, args.output_file)
