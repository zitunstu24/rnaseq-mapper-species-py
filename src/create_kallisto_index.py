import subprocess
import os

def create_kallisto_index(reference_genome, annotation_file, output_dir):
    """
    Create a kallisto index from the reference genome and annotation file.

    :param reference_genome: Path to the reference genome file (e.g., reference.fa).
    :param annotation_file: Path to the annotation file (e.g., annotation.gtf).
    :param output_dir: Path to the output directory where the kallisto index will be stored.
    """
    # Define the output path for the kallisto index
    kallisto_index_path = os.path.join(output_dir, "kallisto_index.idx")
    
    # Build the kallisto index using the reference genome and annotation file
    kallisto_build_cmd = ["kallisto", "index", "-i", kallisto_index_path, reference_genome]
    subprocess.run(kallisto_build_cmd, check=True)
    
    print(f"Kallisto index created at: {kallisto_index_path}")
    
    return kallisto_index_path
