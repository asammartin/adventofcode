
FORWARD = "forward"
BACKWARD = "backward"
DOWN = "down"
UP = "up"

x = 0
y = 0
aim = 0
with open("day2-2.data") as f:
    for (direction, depth) in [line.split() for line in f]:
        if (direction.strip() == FORWARD):
            v = int(depth.strip())
            x += v
            y += aim * v
        elif (direction.strip() == DOWN):
            v = int(depth.strip())
            # y += v
            aim += v
        elif (direction.strip() == UP):
            v = int(depth.strip())
            # y -= v
            aim -= v

        print(f"{direction}, {depth} - {x}, {y}, {aim}")

print(f"{x}, {y}, {aim}, {x * y}")
