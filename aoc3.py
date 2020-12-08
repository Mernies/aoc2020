import numpy as np

N = 323
numlist = np.empty((N,1))

currColIdx = np.empty((5,1)) # keep track of current column, row doesn't matter
numTrees = np.empty((5,1))
firstRow = 1
rowLength = 0
i = 0
for line in open('input3.txt'):
   if line.strip():           # line contains eol character(s)
       if firstRow:
          rowLength = len(line) - 1
          #print('ROW LENGTH: ' + str(rowLength))
          firstRow = 0
          continue
       i = i + 1
       line = line[:-1]
       for j in range(5):
           if j == 4 and i % 2 == 1:
               continue
           increment = j*2 + 1
           if j == 4:
               increment = 1
           currColIdx[j] = currColIdx[j] + increment
           if currColIdx[j] > rowLength - 1: # wraparound if overflow
              currColIdx[j] = currColIdx[j] - rowLength
           idx = int(currColIdx[j])
           if line[idx] == '#':
              numTrees[j] = numTrees[j] + 1

output = 'Part 1: ' + str(numTrees[1]) + ' trees'
print(output)
output = 'Part 2: ' + str(np.prod(numTrees)) + ' trees'
print(output)