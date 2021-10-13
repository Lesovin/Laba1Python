
import os
import zipfile

#os.mkdir("unpacked")
directory_to_extract_to = os.path.abspath("unpacked")
arch_file = "D:\\archive.zip"
zip_archive = zipfile.ZipFile(arch_file)
zip_archive.extractall(directory_to_extract_to)
zip_archive.close()
path=os.path.abspath(".idea")
print(path)
