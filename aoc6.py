N = 800
outputSum = 0
outputSumCommon = 0
groupAnswers = ''
groupAnswersCommon = ''
tempgroupAnswers = ''
firstPerson = 1
for line in open('input6.txt'):
    if line.strip():           # line contains eol character(s)
        #part 1
        for letter in line[:-1]:
            if letter not in groupAnswers:
                groupAnswers = groupAnswers + letter
        #part 2
        if firstPerson == 1:
            groupAnswersCommon = line[:-1]
            firstPerson = 0
        else:
            for letter in line[:-1]:
                if letter in groupAnswersCommon:
                    tempgroupAnswers = tempgroupAnswers + letter
            groupAnswersCommon = tempgroupAnswers
            tempgroupAnswers = ''
    else:
        outputSum = outputSum + len(groupAnswers)
        groupAnswers = ''
        #part 2
        outputSumCommon = outputSumCommon + len(groupAnswersCommon)
        groupAnswersCommon = ''
        firstPerson = 1
outputSum = outputSum + len(groupAnswers)
groupAnswers = ''
#part 2
outputSumCommon = outputSumCommon + len(groupAnswersCommon)
groupAnswersCommon = ''
          
output = 'Part 1: '+str(outputSum)
print(output)
output2 = 'Part 2: '+str(outputSumCommon)
print(output2)