
bagDick = {}; # key is bag that fits in all bags in values
for line in open('input7.txt'):
    if line.strip():           # line contains eol character(s)
        #part 1, just store colors
        temp = line.split(' ')
        value = temp[0] + ' ' + temp[1]
        if temp[4] == 'no':
            continue
        key = temp[5] + ' ' + temp[6]
        if key in bagDick:
            bagDick[key] = bagDick[key] + ',' + value
        else:
            bagDick[key] = value
        bagTerm = temp[7]
        bagidx = 7
        while ',' in bagTerm:
            key = temp[bagidx+2] + ' ' + temp[bagidx+3]
            bagTerm = temp[bagidx+4]
            bagidx = bagidx + 4
            if key in bagDick:
                bagDick[key] = bagDick[key] + ',' + value
            else:
                bagDick[key] = value

# look for shiny gold
toDoList = 'shiny gold'
completedList = {};
while toDoList != '':
    if ',' in toDoList:
        bagTypes = toDoList.split(',')
        numItems = len(bagTypes)
        toDoList = ''
        for item in bagTypes:
            if item not in completedList:
                completedList[item] = 0
            if item in bagDick:
                if bagDick[item] not in toDoList:
                    toDoList = toDoList + bagDick[item] + ','
        toDoList = toDoList[:-1] #remove last comma
    else:
        item = toDoList
        toDoList = ''
        if item not in completedList:
            completedList[item] = 0
            if item in bagDick:
                toDoList = bagDick[item]
        
output = 'Part 1: '+str(len(completedList)-1) #need to subtract shiny gold entry since it can't contain itself
print(output)


def stupidRecursion(key,dictionary):
    if key in dictionary:
        if ',' in dictionary[key]:
            totalBags = 0
            vals = dictionary[key].split(',')
            for item in vals:
                temp = item.split('*')
                numBags = int(temp[0])
                newBag = temp[1]
                tempBags = numBags * stupidRecursion(newBag,dictionary)
                totalBags = totalBags + tempBags
            return totalBags + 1
        else:
            temp = dictionary[key].split('*')
            numBags = int(temp[0])
            newBag = temp[1]
            tempBags = 1 + numBags * stupidRecursion(newBag,dictionary)
            return tempBags
    else:
        return 1
    
# Part 2
bagDick = {}; # key stores other bag colors along with values
for line in open('input7.txt'):
    if line.strip():           # line contains eol character(s)
        #part 1, just store colors
        temp = line.split(' ')
        key = temp[0] + ' ' + temp[1]
        if temp[4] == 'no':
            continue
        value = temp[4] + '*' + temp[5] + ' ' + temp[6]
        bagTerm = temp[7]
        bagidx = 7
        while ',' in bagTerm:
            value = value + ',' + temp[bagidx+1] + '*' + temp[bagidx+2] + ' ' + temp[bagidx+3]
            bagTerm = temp[bagidx+4]
            bagidx = bagidx + 4
        bagDick[key] = value

target = 'shiny gold'
part2Bags = stupidRecursion(target,bagDick)-1 # need to subtract 1 otherwise the answer is wrong
output2 = 'Part 2: '+str(part2Bags)
print(output2)