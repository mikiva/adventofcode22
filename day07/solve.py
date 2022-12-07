import os
import re
import sys
from collections import defaultdict

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"
lines = open(f).read().split("\n")
dirs = defaultdict(list)
cwd = ""
for line in lines:
    l = line.split(" ")
    if l[0] == "$":
        cmd = l[1]
        if cmd == "cd":
            if re.match(r"\w", l[2]):
                if cwd == "/":
                    cwd = ""
                cwd += "/" + l[2]
            elif l[2] == "/":
                cwd = "/"
            else:
                cwd = "/".join(cwd.split("/")[:-1])

            if cwd not in dirs.keys():
                dirs[cwd] = list()
    elif l[0].isdigit():
        keys = dirs.keys()
        dirs[cwd].append(int(l[0]))
        for k in keys:
            if k in cwd and cwd != k:
                dirs[k].append(int(l[0]))

sizes = 0
for dir, s in dirs.items():
    sub = sum(s)
    if sub <= 100_000:
        sizes += sub

total_disk_space = 70_000_000
unused_needed = 30_000_000
current_unused = total_disk_space - sum(dirs["/"])
delete_needed = unused_needed - current_unused
cur = sys.maxsize
to_delete = {}
for d, content in dirs.items():
    size = sum(content)
    if size > delete_needed:
        to_delete[d] = size



print("p1", sizes)
print("p2", min(to_delete.values()))
