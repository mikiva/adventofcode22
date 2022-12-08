import os
from collections import defaultdict

f = f"../inputs/{os.path.split(os.getcwd())[1]}_ex.txt"
input_lines = [[dict(h=int(t), visits=0) for t in tree_line] for tree_line in open(f).read().split("\n")]


def rotate(grid):
    return list([l for l in zip(*grid[::-1])])


lines = input_lines
for _ in range(4):
    for row in lines:
        height = -1
        for col in row:
            if (h := col.get("h")) > height:
                height = h
                col["visits"] += 1

    lines = rotate(lines)

visits = 0
v = sum([len([c for c in row if c["visits"] > 0]) for row in lines])
print("p1", v)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # RIGHT, DOWN, LEFT, UP
candidates = []
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        col['coors'] = (i, j)
        candidates.append(col)

wi, wj = len(lines)-1, len(lines[0])-1

highest = 1
scores = []
for candidate in candidates:
    score = 1
    cheight = candidate["h"]
    for x,y in directions:
        dir_score = 0
        #for i,j in candidate["coors"]:
        ni,nj = candidate["coors"]

        while True:
            ni, nj = (ni+x, nj+y)
            if ni < 0 or nj < 0 or ni > wi or nj > wj:
                break
            if cheight <= lines[ni][nj]["h"]:
                break

            dir_score += 1

        score *= dir_score
        print(candidate["h"], candidate["coors"], dir_score, end=", ")

    print()
    scores.append(score)
    #highest = score if score > highest else highest
print(max(scores))


#for each candidate
#check all directions
# count trees


# for x, y, dx, dy in directions:
#     height = 0
#     while True:
#         h = lines[x][y]
#         if h > height:
#             height = h
#             seen[(x, y)] = height
#         else:
#             break
#

# # L -> R
# for i, row in enumerate(lines):
#     height = row[0]
#     seen[(i, 0)] = height
#     for j, tree in enumerate(row[1:]):
#         if tree > height:
#             height = tree
#             seen[(i, j)] = height
#         else:
#             break
#
# # L <- R
# for i, row in enumerate(lines[1:]):
#     height = row[-1]
#     seen[(i, 0)] = height
#
#     for j in range(len(row) - 2, 1, -1):
#         tree = row[j]
#         if tree > height:
#             height = tree
#             seen[(i, j)] = height
#
#         else:
#             break
#
# # U -> D
# for j, col in enumerate(lines[0]):
#     height = col
#     seen[(0, j)] = height
#     for i, row in enumerate(lines[1:]):
#         tree = row[i]
#         if tree > height:
#             height = tree
#             seen[(i, j)] = height
#         else:
#             break
# # U <- D
# for j, col in enumerate(lines[0]):
#     height = col
#     seen[(len(lines) - 1, j)] = height
#     for i in range(len(lines) - 2, 1, -1):
#         tree = lines[i][j]
#         if tree > height:
#             height = tree
#             seen[(i, j)] = height
#         else:
#             break

# 456 too low
# 1245 too low
# 1504 too low
# 1773 wrong
print("=======")
