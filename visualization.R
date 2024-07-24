library(ggplot2)
library(optparse)

# Define command-line arguments
option_list <- list(
  make_option(c("-i", "--input_file"), type="character", default="genome_data.csv", 
              help="Path to the input CSV file", metavar="character"),
  make_option(c("-o", "--output_file"), type="character", default="genome_plot.png", 
              help="Path to the output PNG file", metavar="character")
)

# Parse command-line arguments
opt_parser <- OptionParser(option_list=option_list)
opt <- parse_args(opt_parser)

# Read the CSV file into a data frame
df <- read.csv(opt$input_file)

# Create the plot
plot <- ggplot(df, aes(x = Genome)) +
  geom_line(aes(y = Core, color = "Core"),  size = 0.9) +
  geom_line(aes(y = Pan, color = "Pan"),  size = 0.9) +
  geom_line(aes(y = Accessory, color = "Accessory"), size = 0.9) +
  labs(x = "Number of Genomes", y = "Number of Distinct Gene Clusters") +
  scale_color_manual(values = c("Core" = "forest green", "Pan" = "blue", "Accessory" = "coral"), 
                     labels = c("Core", "Pan", "Accessory"))

#Save the plot
ggsave(opt$output_file, plot = plot, width = 10, height = 6, dpi = 300)

