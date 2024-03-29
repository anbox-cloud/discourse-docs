import requests, json
import sys
import subprocess

if len(sys.argv) != 2:
    print("You must provide the PR number!")
    exit(1)
else:
    pr = sys.argv[1]

    url = requests.get("https://api.github.com/repos/anbox-cloud/discourse-docs/pulls/"+pr+"/files?per_page=100")
    data = json.loads(url.text)

    for one in data:
        filename = one['filename']
        if (filename == "ref/ams-configuration.yaml") or (filename == "ref/ams-configuration.tmpl.md"):
            filename = "ref/ams-configuration.md"
        print("Publish "+filename)
        subprocess.call("./publish.sh "+filename, shell=True)
