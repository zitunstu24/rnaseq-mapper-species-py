import subprocess
import os

def run_kallisto(sra_id, data_dir, kallisto_index, output_dir):
    """Run kallisto quantification."""
    cmd = [
        "kallisto", "quant",
        "-i", kallisto_index,
        "-o", output_dir,
        os.path.join(data_dir, f"{sra_id}_1.fastq"),
        os.path.join(data_dir, f"{sra_id}_2.fastq")
    ]
    subprocess.run(cmd, check=True)
