import numpy as np

def isValid(numList,value):
    for i in range(0,24):
        for j in range(1,25):
            if numList[i] + numList[j] == value:
                return 1
    return 0

numList = [];
i = 0
badNum = 0
for line in open('input9.txt'):
    if line.strip():           # line contains eol character(s)
        numList.append(int(line[:-1]))
        if i >= 25:
            if not isValid(numList,numList[-1]):
                badNum = numList[-1]
                break
            numList.pop(0)
        i += 1
output = 'Part 1: '+str(badNum)
print(output)
        
#part 2
fullList = np.empty((1000,1));
i = 0
for line in open('input9.txt'):
    if line.strip():           # line contains eol character(s)
        fullList[i] = int(line) # need for part 2
    i += 1

weakNum = 0
for j in range(0,999):
    total = 0
    idx = 0
    while total < badNum and j+idx < 1000:
        total += fullList[j+idx]
        idx += 1
    if total == badNum:
        weakNum = np.amax(fullList[j:j+idx]) + np.amin(fullList[j:j+idx])
        break
        
output = 'Part 2: '+str(weakNum)
print(output)