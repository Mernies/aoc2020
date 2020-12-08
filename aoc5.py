import numpy as np
import math

def binary_search(inputstr, minVal, maxVal):
    for FB in inputstr:
        midpoint = (maxVal + minVal-1)/2
        if FB == 'F' or FB == 'L':
            maxVal = midpoint
            midpoint = minVal # need this for final value
        else:
            minVal = midpoint+1
            midpoint = maxVal
        
    return midpoint

N = 799

maxSeatId = 0
seatIds = np.empty((N,1))
i = 0
for line in open('input5.txt'):
    if line.strip():           # line contains eol character(s)
        line = line[:-1]
        rowChars = line[:7]
        colChars = line[-3:]
        row = binary_search(rowChars, 0, 127)
        col = binary_search(colChars, 0, 7)
        seat = row * 8 + col
        seatIds[i] = seat
        if seat > maxSeatId:
            maxSeatId = seat
        i = i + 1

sortedSeats = np.sort(seatIds,axis=None)
for j in range(int(sortedSeats[0]), int(sortedSeats[-1])):
    if j in sortedSeats.astype(int):
        continue
    else:
        output2 = 'Part 2: '+str(j)
        break
output = 'Part 1: '+str(maxSeatId)
print(output)
print(output2)
