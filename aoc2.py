import numpy as np

N = 1000
numlist = np.empty((N,1))

numvalid = 0
numvalid2 = 0
for line in open('input2.txt'):
   if line.strip():           # line contains eol character(s)
       #part 1
       temp = line.split(':')
       password = temp[1]
       temp2 = temp[0].split('-')
       temp3 = temp2[1]
       letter = temp3[-1]
       maxnum = int(temp3[:-1])
       minnum = int(temp2[0])
       numcounts = password.count(letter)
       if numcounts >= minnum and numcounts <= maxnum:
          numvalid = numvalid + 1
          
       #part 2
       #password starts with a space so no need to change indices
       if password[minnum] == letter and password[maxnum] != letter or password[minnum] != letter and password[maxnum] == letter:
          numvalid2 = numvalid2 + 1
          

output = 'Part 1: ' + str(numvalid) + ' valid passwords'
print(output)
output2 = 'Part 2: ' + str(numvalid2) + ' valid passwords'
print(output2)