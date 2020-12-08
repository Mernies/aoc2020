import numpy as np

N = 200
numlist = np.empty((200,1))

i = 0
for line in open('input.txt'):
   if line.strip():           # line contains eol character(s)
       numlist[i] = int(line)          # assuming single integer on each line
       #print(str(numlist[i]))
       i = i + 1
       
# find 2 numbers
targetnumber = 2020
numlist = np.sort(numlist,axis=None)
print(numlist)
done = 0
for i in range(0,199):
    num1 = numlist[i]
    for j in range(i+1,199):
        num2 = numlist[j]
        #print(num2)
        if num1 + num2 == targetnumber:
            output = str(num1)+' * '+str(num2)+' = '+str(num1 * num2)
            print(output)
            done = 1
            break
        elif num1 + num2 > targetnumber:
            break
    if(done):
        break
        
# find 3 numbers
targetnumber = 2020
done = 0
for i in range(0,199):
    num1 = numlist[i]
    for j in range(i+1,199):
        num2 = numlist[j]
        for k in range(i+2,199):
            num3 = numlist[k]
            if num1 + num2 + num3 == targetnumber:
                output = str(num1)+' * '+str(num2)+' * '+str(num3)+' = '+str(num1 * num2 * num3)
                print(output)
                done = 1
                break
            elif num1 + num2 + num3 > targetnumber:
                break
        if done or num1 + num2 >= targetnumber:
            break