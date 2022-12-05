rows = []
with open("day5.stacks.data") as f:
    for line in f:
        rows.append(line)
stackNames = rows.pop(-1).split()
stacks = []
first = True
for row in reversed(rows):
    for idx, col in enumerate(stackNames):
        if first:
            stacks.append([])
        box = row[(idx * 4) + 1].strip()
        if box:
            stacks[idx].append(box)
    first = False
print(stacks)
with open("day5.instructions.data") as f:
    for line in f:
        instructions = line.split()
        moveCnt = int(instructions[1])
        fromIdx = int(instructions[3])
        toIdx = int(instructions[5])
        boxes = stacks[fromIdx - 1][-moveCnt:]
        del stacks[fromIdx - 1][-moveCnt:]
        stacks[toIdx - 1].extend(boxes)
print(stacks)
output = ""
for stack in stacks:
    output += stack[len(stack) - 1]
print(output)
