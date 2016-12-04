numpad  = [[0 for x in range(3)] for y in range(3)]
current = [1, 1]
code = []

file = open("input.txt")
inp = file.read()
instruction_set = inp.split("\n")

number = 1
for i in range(0, 3):
    for x in range(0, 3):
        numpad[i][x] = number
        number += 1

def move(direction, numpad, current):
    if c == "U":
        if current[0] <= 0:
            return
        else:
            current[0] -= 1
    elif c == "D":
        if current[0] >= 2:
            return
        else:
            current[0] += 1
    elif c == "L":
        if current[1] <= 0:
            return
        else:
            current[1] -= 1
    elif c == "R":
        if current[1] >= 2:
            return
        else:
            current[1] += 1

for i in instruction_set:
    for c in i:
        move(c, numpad, current)
    code.append(numpad[current[0]][current[1]])

print("The pin is:", end=' ')
for i in code:
    print(i, end='')