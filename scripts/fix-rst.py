import sys
import re
from files import file_info

output = []
in_table = 0
full_table = ""

keep_anonymous_links = ["LXD", "Juju documentation", "here", "bundle.yaml", "upstream 90.0.4430.91 release"]

def file_id(file_name):
    return file_name.replace("/","_")[:-4]

urls = [u[-5:] for (t,u,p,n) in file_info.values()]

def replace_link(match, line):

    fixed_title = match.group(1).replace("`","")

    if match.group(2).startswith("https://discourse.ubuntu.com") and match.group(2)[-5:] in urls:
        found = [(key,t) for (key, (t,u,p,n)) in file_info.items() if u[-5:] == match.group(2)[-5:]]

        if match.group(1) == found[0][1]:
            line = line.replace("`"+match.group(1)+" <"+match.group(2)+">`__",":ref:`"+file_id(found[0][0])+"`")
        else:
            line = line.replace("`"+match.group(1)+" <"+match.group(2)+">`__",":ref:`"+fixed_title+" <"+file_id(found[0][0])+">`")


    elif match.group(2).startswith("https://discourse.ubuntu.com") and match.group(2).find("#") > 0:
        found_at = match.group(2).find("#")
        link_id = match.group(2)[found_at+1:]
        url_id = match.group(2)[found_at-5:found_at]
        found = [(key,t) for (key, (t,u,p,n)) in file_info.items() if u[-5:] == url_id]
        link_file = found[0][0]

        line = line.replace("`"+match.group(1)+" <"+match.group(2)+">`__",":ref:`"+fixed_title+" <"+file_id(link_file)+"-"+link_id+">`")

    elif match.group(2).startswith("#"):
        line = line.replace("`"+match.group(1)+" <"+match.group(2)+">`__",":ref:`"+fixed_title+" <"+file_id(file_name)+"-"+match.group(2).lstrip("#")+">`")


    else:
        if match.group(1) in keep_anonymous_links:
            return line
        else:
            line = line.replace("`"+match.group(1)+" <"+match.group(2)+">`__","`"+match.group(1)+" <"+match.group(2)+">`_")
            #print("Not replaced: "+match.group(2))

    return line


with open(sys.argv[1], 'r') as rst_file:

    file_name = sys.argv[1].replace("./","")

    # add ID
    output.append(".. _"+file_id(file_name)+":\n\n")

    # add title
    if file_name in file_info:
        title = file_info[file_name][0]
    else:
        print("Missing in file_info: "+file_name)
        exit()
    for i in title:
        output.append("=")
    output.append("\n"+title+"\n")
    for i in title:
        output.append("=")
    output.append("\n\n")


    note = 0

    for line in rst_file:

        # find note start
        match = re.match(r"^( *)\[note type=“.+?” status=“(.+)”\](.*)$", line)

        if match:
            note = 1
            if match.group(2) == "Note":
                output.append(match.group(1)+".. note::\n")
            elif match.group(2) == "Caution":
                output.append(match.group(1)+".. caution::\n")
            elif match.group(2) == "Tip":
                output.append(match.group(1)+".. tip::\n")
            elif match.group(2) == "Hint":
                output.append(match.group(1)+".. hint::\n")
            elif match.group(2) == "Important":
                output.append(match.group(1)+".. important::\n")
            elif match.group(2) == "Warning":
                output.append(match.group(1)+".. warning::\n")
            else:
                print("Unknown admonition: "+match.group(2))
            output.append(match.group(1)+"   "+match.group(3).strip(" \n")+"\n")
            continue

        if line.endswith("[/note]\n"):
            note = 2
            line = line.replace("[/note]","")

        # find REPLACEID- (was: <a name ...)
        match2 = re.match(r"^REPLACEID-(.+) *$", line)

        if match2:
            output.append(".. _"+file_id(file_name)+"-"+match2.group(1).replace("MINUSMINUS","--")+":\n")
            continue

        if note:
            output.append("   ")

        # Fix wrong code type
        line = line.replace(".. code:: json",".. code::")
        line = line.replace(".. code:: payload",".. code::")

        # Fix/hack details

#        match3 = re.match(r"\[Details=(.+)\]", line)

#        if match3:
#            output.append("\n.. raw:: html\n\n   <details>\n   <summary><a>"+match3.group(1)+"</a></summary>\n\n")
#            continue

#        line = line.replace("[/Details]",".. raw:: html\n\n   </details>")


        # Fix tables

        if line.startswith("TABLEHEADER"):

            in_table = 1
            full_table = line.rstrip("\n")
            continue

        if line.find("TABLEEND") > -1 and in_table:

            full_table += " "+line.rstrip("\n")
            in_table = 0

            table = full_table.split("#X#")
            first_in_row = 0

            for field in table:
                if field == "TABLEHEADER":
                    output.append("\n.. list-table::\n   :header-rows: 1\n\n")
                    output.append("   * ")
                    first_in_row = 1
                elif field =="TABLEROW":
                    output.append("\n   * ")
                    first_in_row = 1
                elif field =="TABLEEND":
                    continue
                elif field.strip():
                    if field == "XEMPTYX":
                        field = ""
                    if first_in_row:
                        output.append("- "+field)
                    else:
                        output.append("\n     - "+field)
                    first_in_row = 0

            output.append("\n\n")
            continue

        if in_table:
            full_table += " "+line.rstrip("\n")
            continue

        # Fix links
        if line.find("`__") >= 0:

            match4 = re.match(r".*? ?`([^<]+) <(.+)>`__", line)

            if not match4:
                line_backup = line
                line_backup1 = output.pop()
                line = line_backup1.rstrip(" \n")+" "+line.lstrip()
                match4 = re.match(r".*? ?`([^<]+) <(.+)>`__", line)

            if match4:
                line = replace_link(match4, line)
            else:
                line_backup2 = output.pop()
                line = line_backup2.rstrip(" \n")+" "+line.lstrip()
                match4 = re.match(r".*? ?`([^<]+) <(.+)>`__", line)

                if match4:
                    line = replace_link(match4, line)
                else:
                    output.append(line_backup2+"\n")
                    output.append(line_backup1+"\n")
                    line = line_backup
                    print("Weird link in "+file_name+": "+line)


        output.append(line)

        if note == 2:
            note = 0



# Create toctree

links = [(key,n) for (key, (t,u,p,n)) in file_info.items() if p == file_name]

if links:
    output.append("\n\n.. toctree::\n   :titlesonly:\n\n")
    links.sort(key=lambda x:x[1])
    for (l,x) in links:
        split_base = file_name.split("/")
        split_l = l.split("/")
        link_name = ""
        if len(split_l)-len(split_base) < 0:
            for i in range(len(split_base)-len(split_l)):
                link_name += "../"
        for i in range(len(split_l)):
            if i >= len(split_base):
                link_name += split_l[i]+"/"
            elif split_base[i] == split_l[i]:
                continue
            elif split_l[i].endswith(".rst"):
                link_name += split_l[i]
            elif split_base[i].endswith(".rst"):
                link_name += split_l[i]+"/"
            else:
                link_name += "../"+split_l[i]+"/"
        link_name = link_name.replace(".rst","")
        output.append("   "+link_name+"\n")

with open(sys.argv[1], 'w') as out_file:
    for line in output:
        out_file.write(line)
