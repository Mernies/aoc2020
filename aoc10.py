import numpy as np

#part 1
numList = np.empty((114,1));
i = 0
for line in open('input10.txt'):
    if line.strip():           # line contains eol character(s)
        numList[i] = int(line) # need for part 2
    i += 1

sortednumList = numList.copy()
sortednumList = np.sort(sortednumList, axis = None)
diffList = np.diff(sortednumList)
ones = np.count_nonzero(diffList == 1)
threes = np.count_nonzero(diffList == 3) + 1 #includes an extra 3 because of built-in adapter
if sortednumList[0] == 1:
    ones += 1
elif sortednumList[0] == 3:
    threes += 1
output = 'Part 1: '+str(ones*threes)
print(output)

#part 2
# 4 1's in a row = 7 choices? where is the 7th
# 0,1,2,3,4
# 0,1,2,4
# 0,1,3,4
# 0,2,3,4
# 0,2,4
# 0,3,4

#
# 3 1's in a row = 4 choices
# 2 1's = 2 choices

count = 1
total = 1
for i in range(0,len(diffList)):
    if diffList[i] == 1:
        count += 1
    elif count == 4:
        total = total * 7
        count = 0
    elif count == 3:
        total = total * 4
        count = 0
    elif count == 2:
        total = total * 2
        count = 0
    else: # only one possible combination for 1
        count = 0
if count == 4:
    total = total * 7
elif count == 3:
    total = total * 4
elif count == 2:
    total = total * 2

output = 'Part 2: ' + str(total)
print(output)