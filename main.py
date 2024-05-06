import os
import yaml
import sys

# Import functions from the src subdirectory
from src.create_kallisto_index import create_kallisto_index
from src.download_fastq import download_fastq
from src.run_kallisto import run_kallisto
from src.move_abundance import move_abundance_file

def main(yml_file):
    # Load YAML configuration file
    with open(yml_file, 'r') as file:
        config = yaml.safe_load(file)
    
    base_dir = config['base_dir']
    data_dir = config['data_dir']
    output_dir = config['output_dir']
    
    # Create directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each genome specified in the YAML file
    for genome in config['genomes']:
        genome_dir = genome['genome_dir']
        genome_name = os.path.basename(genome_dir)
        
        # Paths for reference genome and kallisto index
        reference_genome = os.path.join(genome_dir, "reference.fa")
        annotation_file = os.path.join(genome_dir, "annotation.gtf")  # Path to the annotation file
        kallisto_index_path = os.path.join(genome_dir, "kallisto_index.idx")
        
        # Create kallisto index if it doesn't exist
        if not os.path.exists(kallisto_index_path):
            kallisto_index_path = create_kallisto_index(reference_genome, annotation_file, genome_dir)
        
        # Path to the file containing SRA IDs for this genome
        sra_file = genome['sra_file']
        
        # Read each SRA ID from the file
        with open(sra_file, 'r') as sra_file_content:
            sra_ids = sra_file_content.read().strip().split()
        
        # Process each SRA ID
        for sra_id in sra_ids:
            # Download SRA sample using fasterq-dump
            download_fastq(sra_id, data_dir)
            
            # Define output directory for this SRA ID
            sra_output_dir = os.path.join(output_dir, genome_name, sra_id)
            
            # Create output directory if it doesn't exist
            os.makedirs(sra_output_dir, exist_ok=True)
            
            # Run kallisto quantification
            run_kallisto(sra_id, data_dir, kallisto_index_path, sra_output_dir)
            
            # Move the abundance file to the desired location
            abundance_file_path = os.path.join(sra_output_dir, "abundance.tsv")
            final_abundance_file_path = os.path.join(output_dir, genome_name, f"{sra_id}_abundance.tsv")
            move_abundance_file(abundance_file_path, final_abundance_file_path, sra_id)
            
            # Optionally, clean up downloaded FASTQ files
            os.remove(os.path.join(data_dir, f"{sra_id}_1.fastq"))
            os.remove(os.path.join(data_dir, f"{sra_id}_2.fastq"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: RnaseqMapper config.yml")
        sys.exit(1)
    
    config_file = sys.argv[1]
    main(config_file)
