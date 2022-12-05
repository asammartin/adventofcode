elfCals = []
with open("day1.data") as f:
    elfCals.append(0)
    for line in f:
        cals = line.strip()
        if not cals:
            elfCals.append(0)
        else:
            elfCals[len(elfCals) - 1] += int(cals)
elfCals.sort(reverse=True)
print(elfCals)
print(elfCals[0])
