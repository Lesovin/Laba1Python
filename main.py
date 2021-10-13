
import os
import zipfile
import hashlib

# os.mkdir("unpacked")
directory_to_extract_to = os.path.abspath("unpacked")
arch_file = "D:\\archive.zip"
zip_archive = zipfile.ZipFile(arch_file)
zip_archive.extractall(directory_to_extract_to)
zip_archive.close()
txt_files=[]
for root, dirs, files in os.walk(directory_to_extract_to):
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(os.path.join(root, file))
print(txt_files)


