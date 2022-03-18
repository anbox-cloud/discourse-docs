import os
import sys
import requests
import tempfile

mapping_file = "file_mapping.txt"
discourse_prefix = "https://discourse.ubuntu.com/"
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

        with tempfile.NamedTemporaryFile(delete=False) as f:
            r = requests.get(discourse_prefix+"raw/"+mapping[filename])
            f.write(r.content)
            oldfile = f.name
            f.close()
            os.system("diff "+oldfile+" "+filename)
            os.unlink(oldfile)

        os.system(editor+" "+filename+"&")
        os.system(discedit+" "+discourse_prefix+"t/"+mapping[filename])
    else:
        print("The file name is not in the mapping file.")
        exit(1)
