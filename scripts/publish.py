import os
import sys
import requests
import tempfile

index_file = "index.md"
index_file_ID = "17029"
discourse_prefix = "https://discourse.ubuntu.com/"
editor = "emacs"
discedit = "discedit"

if "EDITOR" in os.environ:
    editor = os.environ['EDITOR']
if "DISCEDIT" in os.environ:
    discedit = os.environ['DISCEDIT']

# mapping contains file names and their Discourse topic IDs
mapping = {index_file: index_file_ID}

# Read the mapping from the index file
with open(index_file,"r") as input:
    nav = 0

    for line in input:
        # Only process content between "Navigation" and "Redirects"
        if line.find("## Navigation") >= 0:
            nav = 1
            continue
        elif line.find("## Redirects") >= 0:
            nav = 0
            continue
        if nav:
            row = line.split("|")
            # If the link is a Discourse topic, use the URL as file name
            # and extract the topic ID
            if len(row) > 3 and row[3].find("discourse.ubuntu.com") >= 0:
                url = row[2].strip()
                ID = row[3].strip()[-6:-1]
                mapping[url+".md"]= ID

if len(sys.argv) != 2:
    print("You must provide one file name!")
    exit(1)
else:
    filename = sys.argv[1]
    # If we know the topic ID for the given file name
    if filename in mapping:

        # Download the current version of the file and diff it to
        # the file on disk
        with tempfile.NamedTemporaryFile(delete=False) as f:
            r = requests.get(discourse_prefix+"raw/"+mapping[filename])
            f.write(r.content)
            f.write(b'\n') # Discourse file is missing a newline at the end
            oldfile = f.name
            f.close()
            os.system("diff "+oldfile+" "+filename)
            os.unlink(oldfile)

        # Open the file on disk in your editor and start discedit on
        # the corresponding topic ID
        os.system(editor+" "+filename+"&")
        os.system(discedit+" "+discourse_prefix+"t/"+mapping[filename])
    else:
        print("The file name is not in the mapping file.")
        exit(1)
