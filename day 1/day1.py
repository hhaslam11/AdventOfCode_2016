# get input, remove unnecessary chars
file = open("input.txt")
inp = file.read()
inp = inp.replace(" ", "")
inp_list = inp.split(',')

direction = "N"  # N, E, S, W
location_x = 0
location_y = 0
first = False
location_x_first = 0
location_y_first = 0
location_history = []

def change_dir(direction, move):
    if move == "L":
        if direction == "N":
            return "W"

        if direction == "E":
            return "N"

        if direction == "S":
            return "E"
        if direction == "W":
            return "S"
    elif move == "R":
        if direction == "N":
            return "E"
        if direction == "E":
            return "S"
        if direction == "S":
            return "W"
        if direction == "W":
            return "N"

def walk(direction, distance):
    global location_x, location_y, location_history

    if direction == "N":
        for i in range(0, int(distance)):
            location_y += 1
            has_been_before(location_x, location_y)
            location_history.append(str(location_x) + "," + str(location_y))
    if direction == "W":
        for i in range(0, int(distance)):
            location_x -= 1
            has_been_before(location_x, location_y)
            location_history.append(str(location_x) + "," + str(location_y))
    if direction == "S":
        for i in range(0, int(distance)):
            location_y -= 1
            has_been_before(location_x, location_y)
            location_history.append(str(location_x) + "," + str(location_y))
    if direction == "E":
        for i in range(0, int(distance)):
            location_x += 1
            has_been_before(location_x, location_y)
            location_history.append(str(location_x) + "," + str(location_y))

def has_been_before(x, y):
    global location_x_first, location_y_first, first
    if first:
        return
    for i in location_history:
        if (str(x) + "," + str(y)) == i:
            location_x_first = x
            location_y_first = y
            first = True
            break


for i in inp_list:
    if i == "\n":
        continue
    direction = change_dir(direction, i[0])
    x = i.replace("R", "")
    x = x.replace("L", "")
    walk(direction, x)

print(abs(location_x) + abs(location_y))
print(abs(location_x_first) + abs(location_y_first))
