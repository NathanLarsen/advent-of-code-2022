import numpy as np

with open("day8/input.txt") as input:
    line = input.readline().strip()
    forest = []
    while(line):
        treeLine = []
        for char in line:
            treeLine.append(int(char))
        forest.append(treeLine)
        line = input.readline().strip()
    visible = np.zeros((len(forest[0]), len(forest)))
    scenic = np.ones((len(forest[0]), len(forest)))
    notHidden = 0
    mostScenic = 0
    for i in range(len(forest[0])):
        for j in range(len(forest)):
            row = i - 1
            col = j - 1
            hiddenTop = False
            hiddenBottom = False
            hiddenRight = False
            hiddenLeft = False
            scenicTop = 0
            scenicBottom = 0
            scenicRight = 0
            scenicLeft = 0
            while(not hiddenTop and row >= 0):
                if(forest[row][j] >= forest[i][j]):
                    hiddenTop = True
                    break
                row -= 1
            if(row < 0):
                row = 0
            scenicTop = abs(i - row)
            row = i + 1
            while(not hiddenBottom and row < len(forest[0])):
                if(forest[row][j] >= forest[i][j]):
                    hiddenBottom = True
                    break
                row += 1
            if(row == len(forest[0])):
                row -= 1
            scenicBottom = abs(i - row)
            while(not hiddenLeft and col >= 0):
                if(forest[i][col] >= forest[i][j]):
                    hiddenLeft = True
                    break
                col -= 1
            if(col < 0):
                col = 0
            scenicLeft = abs(j - col)
            col = j + 1
            while(not hiddenRight and col < len(forest)):
                if(forest[i][col] >= forest[i][j]):
                    hiddenRight = True
                    break
                col += 1
            if(col == len(forest[0])):
                col -= 1
            scenicRight = abs(j - col)
            visible[i][j] = not hiddenTop or not hiddenBottom or not hiddenLeft or not hiddenRight
            if(visible[i][j]):
                notHidden += 1
            scenic[i][j] = scenicTop * scenicBottom * scenicLeft * scenicRight
            if(scenic[i][j] > mostScenic):
                mostScenic = scenic[i][j]
    print(notHidden)
    print(mostScenic)