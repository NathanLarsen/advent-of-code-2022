# with open('input.txt', 'r', encoding='utf-8') as input:
#     iWin = {'A':'Y', 'B':'Z', 'C':'X'}
#     youWin = {'X':'B', 'Y':'C', 'Z':'A'}
#     points = {'X': 1, 'Y': 2, 'Z': 3}
#     score = 0
#     for line in input.readlines():
#         plays = line.strip().split(' ')
#         you = plays[0]
#         me = plays[1]
#         if(me == iWin[you]):
#             score += 6
#         elif(you == youWin[me]):
#             score += 0
#         else:
#             score += 3
#         score += points[me]
#     print(score)
with open('input.txt', 'r', encoding='utf-8') as input:
    iWin = {'A':'Y', 'B':'Z', 'C':'X'}
    youWin = {'B':'X', 'C':'Y', 'A':'Z'}
    draw = {'A':'X', 'B':'Y', 'C':'Z'}
    myPoints = {'X':1, 'Y':2, 'Z':3}
    points = {'X': 0, 'Y': 3, 'Z': 6}
    score = 0
    for line in input.readlines():
        plays = line.strip().split(' ')
        you = plays[0]
        outcome = plays[1]
        if outcome == 'X':
            score += myPoints[youWin[you]]
        if outcome == 'Y':
            score += myPoints[draw[you]]
        if outcome == 'Z':
            score += myPoints[iWin[you]]
        score += points[outcome]
    print(score)