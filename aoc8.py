
cmdList = []
for line in open('input8.txt'):
    if line.strip():           # line contains eol character(s)
        #part 1, store (command, value)
        cmdList.append((line[:3], line[4:-1]))
#print(cmdList)

curridx = 0
usedIdxList = []
accum = 0
while 1:
    if curridx in usedIdxList:
        break
    usedIdxList.append(curridx)
    cmd = cmdList[curridx][0]
    val = int(cmdList[curridx][1])
    #print(cmdList[curridx])
    if cmd == 'acc':
        accum += val
        curridx += 1
        #print('acc')
    elif cmd == 'jmp':
        curridx += val
        #print('jmp')
    else:
        curridx += 1
        #print('nop')
    print(curridx)
        
output = 'Part 1: '+str(accum)
print(output)

output2 = 'Part 2: '+str(part2Bags)
print(output2)