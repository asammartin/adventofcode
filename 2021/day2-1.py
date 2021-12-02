
FORWARD = "forward"
BACKWARD = "backward"
DOWN = "down"
UP = "up"

x = 0
y = 0
with open("day2-1.data") as f:
    for (direction, depth) in [line.split() for line in f]:
        if (direction.strip() == FORWARD):
            x += int(depth.strip())
        elif (direction.strip() == BACKWARD):
            x -= int(depth.strip())
        elif (direction.strip() == DOWN):
            y += int(depth.strip())
        elif (direction.strip() == UP):
            y -= int(depth.strip())

        print(f"{direction}, {depth}")

print(f"{x}, {y}, {x * y}")
