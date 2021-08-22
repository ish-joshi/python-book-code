import json
import os

folders = ["lists-iterables"]

files = []

for folder in folders:
    files_in_folder = os.listdir(folder)
    md_files = filter(lambda file: file.endswith(".md"), files_in_folder)
    md_files = map(lambda fn: f"{folder}/{fn}", md_files)
    files.extend(md_files)

print(files)

output = {}

for md_file in files:
    folder, filename = md_file.split("/")
    filename_withoutextension = filename.split(".")[0]
    file = open(md_file)
    contents = file.read()
    output[filename_withoutextension] = contents

with open("out.json", "w") as outfile:
    outfile.write(json.dumps(output))


