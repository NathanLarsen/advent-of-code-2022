    # [C]             [L]         [T]
#     [V] [R] [M]     [T]         [B]
#     [F] [G] [H] [Q] [Q]         [H]
#     [W] [L] [P] [V] [M] [V]     [F]
#     [P] [C] [W] [S] [Z] [B] [S] [P]
# [G] [R] [M] [B] [F] [J] [S] [Z] [D]
# [J] [L] [P] [F] [C] [H] [F] [J] [C]
# [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
#  1   2   3   4   5   6   7   8   9 
# with open('day5/input.txt', 'r', encoding='utf-8') as input:
#     stacks = [
#         ['G', 'J', 'Z'],
#         ['C','V','F','W','P','R','L','Q'],
#         ['R','G','L','C','M','P','F'],
#         ['M','H','P','W','B','F','L'],
#         ['Q','V','S','F','C','G'],
#         ['L','T','Q','M','Z','J','H','W'],
#         ['V','B','S','F','H'],
#         ['S','Z','J','F'],
#         ['T','B','H','F','P','D','C','M']
#         ]
#     for i in range(10):
#         print(input.readline())
#     line = input.readline()
#     while(line):
#         words = line.strip().split(' ')
#         crates = int(words[1])
#         fromStack = int(words[3]) - 1
#         toStack = int(words[5]) - 1
#         for i in range(crates):
#             crate = stacks[fromStack].pop(0)
#             stacks[toStack].insert(0, crate)
#         line = input.readline()
#     print(stacks)
with open('day5/input.txt', 'r', encoding='utf-8') as input:
    stacks = [
        ['G', 'J', 'Z'],
        ['C','V','F','W','P','R','L','Q'],
        ['R','G','L','C','M','P','F'],
        ['M','H','P','W','B','F','L'],
        ['Q','V','S','F','C','G'],
        ['L','T','Q','M','Z','J','H','W'],
        ['V','B','S','F','H'],
        ['S','Z','J','F'],
        ['T','B','H','F','P','D','C','M']
        ]
    for i in range(10):
        print(input.readline())
    line = input.readline()
    while(line):
        words = line.strip().split(' ')
        crates = int(words[1])
        fromStack = int(words[3]) - 1
        toStack = int(words[5]) - 1
        cratesToMove = []
        for i in range(crates):
            cratesToMove.insert(0, stacks[fromStack].pop(0))
        for i in range(crates):
            stacks[toStack].insert(0, cratesToMove.pop(0))
        line = input.readline()
    print(stacks)