import sys
import re

output = []

with open(sys.argv[1], 'r') as md_file:
    for line in md_file:

        match = re.match(r"^(.*)\[(.*)`(.+)`(.*)\]\((.*)$", line)

        if match:
            output.append(match.group(1)+"["+match.group(2)+match.group(3)+match.group(4)+"]("+match.group(5)+"\n\n")

        else:
            output.append(line)


with open(sys.argv[1], 'w') as out_file:
    for line in output:
        out_file.write(line)
