import os

f = f"../inputs/{os.path.split(os.getcwd())[1]}_ex.txt"

def play(a, b) -> int:
    b = "XYZ".index(b)
    a = "ABC".index(a)
    s = b + 1

    outcome = (b - a) % 3
    print(outcome)
    if outcome == 0:
        return 3 + s
    elif outcome == 1:
        return 6 + s
    else:
        return 0 + s


def play_mod(a, b) -> int:
    s = "ABC".index(a)

    if b == "X":
        return (s - 1) % 3 + 1
    elif b == "Y":
        return 3 + s + 1
    else:
        return 6 + (s + 1) % 3 + 1


i = [g.strip() for g in open(f).readlines()]
score = 0
score2 = 0
for game in i:
    a, b = game.split()
    s = play(a, b)
    score += s

    s2 = play_mod(a, b)
    score2 += s2

print("p1", score)
print("p2", score2)
#assert score == 12855
#assert score2 == 13726
#