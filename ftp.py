from ftplib import FTP
import hashlib
import toml


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


config = toml.load("config.toml")

ip_address = config["ip"]["address"]
username = config["ip"]["username"]
password = config["ip"]["password"]

ftp = FTP()
ftp.connect(ip_address, 21)
ftp.login(username, password)

with open("archive.zip", "rb") as f:
    ftp.storbinary("STOR archive.zip", f)

# Скачивание архива с сервера для проверки
with open("downloaded_archive.zip", "wb") as f:
    ftp.retrbinary("RETR archive.zip", f.write)

# Вычисление и сравнение чексумм
original_checksum = md5("archive.zip")
downloaded_checksum = md5("downloaded_archive.zip")

print(f"Original checksum: {original_checksum}")
print(f"Downloaded checksum: {downloaded_checksum}")

if original_checksum == downloaded_checksum:
    print("Checksums match. File transfer is successful.")
else:
    print("Checksums do not match. File transfer is not successful.")

ftp.quit()
