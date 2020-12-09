cmdList = []
for line in open('input8.txt'):
    if line.strip():           # line contains eol character(s)
        cmdList.append((line[:3], line[4:-1]))

numCommands = len(cmdList)
swapidx = -99
part2 = 0
for i in range(0,numCommands):
    tempcmdList = cmdList.copy()
    cmd = cmdList[i][0]
    val = cmdList[i][1]
    if cmd == 'jmp':
        tempcmdList[i] = ('nop',val)
    elif cmd == 'nop':
        tempcmdList[i] = ('jmp',val)
    else:
        continue
    curridx = 0
    usedIdxList = []
    accum = 0
    while 1:
        if curridx in usedIdxList:
            break
        elif curridx == numCommands:
            swapidx == i
            part2 = accum
            break
        usedIdxList.append(curridx)
        cmd = tempcmdList[curridx][0]
        val = int(tempcmdList[curridx][1])
        if cmd == 'acc':
            accum += val
            curridx += 1
        elif cmd == 'jmp':
            curridx += val
        else:
            curridx += 1
    if swapidx > 0:
        break
        
output = 'Part 2: '+str(part2)
print(output)