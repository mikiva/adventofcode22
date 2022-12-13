import os
import re
from functools import lru_cache

print("START==========")

f = f"../inputs/{os.path.split(os.getcwd())[1]}_ex"
pairs = open(f).read().split("\n\n")
print(*pairs, sep="\n")

print("=================")
