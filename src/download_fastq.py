import subprocess

def download_fastq(sra_id, data_dir):
    """Download FASTQ files for the given SRA ID."""
    cmd = ["fasterq-dump", "--outdir", data_dir, "--split-files", sra_id]
    subprocess.run(cmd, check=True)
