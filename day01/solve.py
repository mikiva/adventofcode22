input = "../inputs/day01.txt"

i = sorted([sum([int(l) for l in line.split()]) for line in open(input, "r").read().split("\n\n")], reverse=True)
print("p1", i[0])
print("p2", sum(i[:3]))
