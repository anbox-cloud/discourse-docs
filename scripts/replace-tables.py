import sys
import re

output = []

in_table = 0

with open(sys.argv[1], 'r') as md_file:

    for line in md_file:

        if line.startswith("----") or line.startswith("---|") or line.startswith("|--"):

            in_table = 1

            table="TABLEHEADER#X#"

            header = output.pop().rstrip("\n").strip("|").split("|")
            for one in header:
                if one.strip():
                    table += one.strip()+"#X#"
                else:
                    table += "XEMPTYX#X#"

        elif in_table:

            row = line.rstrip("\n").strip("|").split("|")
            if len(row) == 1:
                in_table = 0
                output.append(table+"TABLEEND\n\n")
            else:
                table += "TABLEROW#X#"
                for one in row:
                    if one.strip():
                        table += one.strip()+"#X#"
                    else:
                        table += "XEMPTYX#X#"

        else:
            output.append(line)


with open(sys.argv[1], 'w') as out_file:
    for line in output:
        out_file.write(line)
