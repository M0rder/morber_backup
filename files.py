from pathlib import Path
import shutil
import hashlib

def calculate_checksum(file_path, chunk_size=8192):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

src_folder = Path("/Users/johndoe/Documents/me_vs_code/exploratory/Morder/presious")
archive_name = Path("archive.zip")

if src_folder.exists() and src_folder.is_dir():
    shutil.make_archive(archive_name.stem, "zip", src_folder)

    archive_path = Path(f"{archive_name.stem}.zip")
    checksum = calculate_checksum(archive_path)

    with open("checksum", "w") as f:
        f.write(checksum)
