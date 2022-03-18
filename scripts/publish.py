import os
import sys

mapping_file = "file_mapping.txt"
discourse_prefix = "https://discourse.ubuntu.com/t/"
editor = "emacs"
discedit = "discedit"

if "EDITOR" in os.environ:
    editor = os.environ['EDITOR']
if "DISCEDIT" in os.environ:
    discedit = os.environ['DISCEDIT']


mapping = {}

with open(mapping_file,"r") as input:

    for line in input:
        one = line.split(":")
        mapping[one[0]]= one[1].strip()

if len(sys.argv) != 2:
    print("You must provide one file name!")
    exit(1)
else:
    filename = sys.argv[1]
    if filename in mapping:
        os.system(editor+" "+filename+"&")
        os.system(discedit+" "+discourse_prefix+mapping[filename])
    else:
        print("The file name is not in the mapping file.")
        exit(1)
