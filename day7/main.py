with open("day7/input.txt") as input:
    line = input.readline()
    path = ['/']
    dirs = {'/_': 0}
    paths = {'/': (1, str(path))}
    line = input.readline()
    while(line):
        if(line.startswith('$')):
            script = line.strip().split(' ')
            if(len(script) == 3):
                dir = script[2]
                if(dir == '..'):
                    path.pop()
                else:             
                    path.append(dir)
                    paths[str(dir) + str(len(path)-1)] = len(path), str(path)
                    thisPath = ""
                    for curDir in path:
                        thisPath += curDir + '_'
                    dirs[thisPath] = 0
        else:
            size, file = line.strip().split(' ')
            if(size != 'dir'):
                size = int(size)
                curPath = ""
                for curDir in path:
                    curPath += curDir + '_'
                    dirs[curPath] += int(size)
        line = input.readline()
    total = 0
    unused = 70000000 - dirs['/_']
    minVal = 40000000
    for dir in dirs:
        if(dirs[dir] <= 100000):
            total += int(dirs[dir])
        if(dirs[dir] + unused >= 30000000):
            minVal = min(minVal,dirs[dir])
    print(total)        
    print(minVal)