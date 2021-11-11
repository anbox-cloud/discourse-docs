import sys
import re

output = []

with open(sys.argv[1], 'r') as md_file:
    for line in md_file:

        match = re.match(r"<a +name=(\"|')(.+)(\"|') *> *</a>", line)

        if match:
            output.append("REPLACEID-"+match.group(2).replace("--","MINUSMINUS")+"\n\n")

        else:
            output.append(line)


with open(sys.argv[1], 'w') as out_file:
    for line in output:
        out_file.write(line)
