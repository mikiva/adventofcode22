import os
import re
from collections import defaultdict

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"

stacks, instructions = [p for p in open(f).read().split("\n\n")]


# BOXES

def get_boxes():
    bs = defaultdict(list)
    boxes_p = r"(\[[A-Z]\])"
    for i, stack in enumerate(stacks.split("\n")[:-1]):
        inds = re.finditer(boxes_p, stack)
        for n in inds:
            val = n.group()
            pos = n.start(0)
            bs[(pos // 4) + 1].insert(0, val)

    return bs


# box_stacks = bs
# INSTRUCTIONS

def p1(box_stacks):
    moves = r"\d+"
    for inst in instructions.split("\n"):
        count, fr, to = [int(i) for i in re.findall(moves, inst)]
        for _ in range(count):
            b = box_stacks[fr].pop()
            box_stacks[to].append(b)

    stack_dicts = sorted(box_stacks.items())

    last_items = "".join([v[-1] for k, v in stack_dicts])
    last_items = last_items.replace("[", "")
    last_items = last_items.replace("]", "")
    return last_items


def p2(box_stacks):
    moves = r"\d+"

    for inst in instructions.split("\n"):
        to_move = []
        count, fr, to = [int(i) for i in re.findall(moves, inst)]
        for _ in range(count):
            to_move.append(box_stacks[fr].pop())
        to_move.reverse()
        box_stacks[to].extend(to_move)
    stack_dicts = sorted(box_stacks.items())

    last_items = "".join([v[-1] for k, v in stack_dicts])
    last_items = last_items.replace("[", "")
    last_items = last_items.replace("]", "")
    return last_items


print("p1", p1(get_boxes()))
print("p2", p2(get_boxes()))
print("===")
