import shutil
import os

def move_abundance_file(src_path, dest_dir, sra_id):
    """
    Move the abundance.tsv file to the desired location and rename it with the respective SRA ID.

    :param src_path: Path to the abundance.tsv file to be moved.
    :param dest_dir: Path to the destination directory where the file will be moved.
    :param sra_id: SRA ID to use as part of the new file name.
    """
    # Create the destination file path with the SRA ID
    dest_path = os.path.join(dest_dir, f"{sra_id}_abundance.tsv")
    
    # Move and rename the abundance.tsv file
    shutil.move(src_path, dest_path)
    print(f"Moved and renamed abundance.tsv to {dest_path}")
