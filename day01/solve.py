def solver(inp, positions):
    elves = []
    cur = 0

    for l in inp:
        if l:
            cur += int(l)
        else:
            elves.append(cur)
            cur = 0
    elves.sort(reverse=True)
    top_calories = sum([c for c in elves[:positions]])
    return top_calories


def solve():
    i = [line for line in open("../inputs/day01.txt", "r").read().split("\n")]
    print(solver(i, 1))
    print(solver(i, 3))


if __name__ == '__main__':
    solve()
