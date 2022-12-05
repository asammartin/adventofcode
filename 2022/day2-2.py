totalScore = 0
with open("day2.data") as f:
    for line in f:
        round = line.strip()
        if not round:
            continue
        round = round.split()
        if not len(round) == 2:
            continue
        outcome = ord(round[1]) - ord('X') - 1
        mePlay = chr((ord(round[0]) - ord('A') + outcome) % 3 + ord('A'))
        opPoints = ord(round[0]) - ord('A')
        mePoints = ord(mePlay) - ord('A')
        roundResult = mePoints - opPoints
        meScore = mePoints + 1
        if abs(roundResult) == 2:
            # edge case loss
            roundResult *= -1
        if roundResult == 0:
            meScore += 3
        elif roundResult > 0:
            meScore += 6
        totalScore += meScore
print(totalScore)
