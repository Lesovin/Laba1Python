
import requests
import re
import os
import zipfile
import hashlib

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
        if hashlib.md5(data).hexdigest() == target_hash:
            target_file = file_path
            target_file_data = open(file_path, 'r').read()
            break
print(target_file)
print(target_file_data)
r = requests.get(target_file_data)
result_dct = {}
counter = 0
lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
for line in lines:
    if counter == 0:
        headers = re.sub(r'(\<(/?[^\>]+)\>)', ';', line)
        headers = re.findall(r'[А-Яа-яёЁ]+\s?', headers)
        print(headers)
        counter += 1
        continue
    temp = re.sub(r'(\<(/?[^\>]+)\>)', ';', line)
    temp = re.sub(r'\([^)]*\)', '', temp)
    temp = re.sub(r'\;+', ';', temp)
    temp = re.sub(r'^;', '', temp)
    temp = re.sub(r';$', '', temp)
    temp = re.sub(r';В', 'В', temp)
    temp = re.sub(r'\*', '', temp)
    temp = re.sub(r'_', '-1', temp)
    temp = re.sub(r'\xa0', '', temp)
    tmp_split = re.split(r';', temp)
    country_name = tmp_split[0]
    col1_val = tmp_split[1]
    col2_val = tmp_split[2]
    col3_val = tmp_split[3]
    col4_val = tmp_split[4]
    result_dct[country_name] = {}
    result_dct[country_name][headers[0]] = col1_val
    result_dct[country_name][headers[1]] = col2_val
    result_dct[country_name][headers[2]] = col3_val
    result_dct[country_name][headers[3]] = col4_val
    counter += 1
