
import os
import zipfile
import hashlib

# os.mkdir("unpacked")
directory_to_extract_to = os.path.abspath("unpacked")
arch_file = "D:\\archive.zip"
zip_archive = zipfile.ZipFile(arch_file)
zip_archive.extractall(directory_to_extract_to)
zip_archive.close()
txt_files = []
for root, dirs, files in os.walk(directory_to_extract_to):
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(os.path.join(root, file))
print(txt_files)
for file in txt_files:
    target_file = file
    target_file_data = open(target_file, 'rb').read()
    result = hashlib.md5(target_file_data).hexdigest()
    print(result)
target_hash = "4636f9ae9fef12ebd56cd39586d33cfb"
target_file = ''
target_file_data = ''
for root, dirs, files in os.walk(directory_to_extract_to):
    for file in files:
        file_path = os.path.join(root, file)
        data = open(file_path, 'rb').read()
        if hashlib.md5(data).hexdigest() == target_hash :
            target_file = file_path
            target_file_data = open(file_path, 'r').read()
            break
print(target_file)
print(target_file_data)

