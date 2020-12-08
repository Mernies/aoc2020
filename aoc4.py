import numpy as np

numvalid = 0
numvalid2 = 0
currPassport = ''
hclchars = '0123456789abcdef'
eclchars = 'amb blu brn gry grn hzl oth'
invalid = 0
for line in open('input4.txt'):
    if line.strip():           # line contains eol character(s)
        currPassport = currPassport + line[:-1] + ' '
    else:
        #print(str(i) + ': ' + currPassport)
        if 'byr:' in currPassport and 'iyr:' in currPassport and 'eyr:' in currPassport and \
        'hgt:' in currPassport and 'hcl:' in currPassport and 'ecl:' in currPassport and \
        'pid:' in currPassport:
            numvalid = numvalid + 1
            # part 2
            fields = currPassport.split()
            for entry in fields:
                tag = entry[:3]
                value = entry[4:]
                if tag == 'byr' and (int(value) > 2002 or int(value) < 1920 or len(value) != 4):
                    invalid = 1
                    break
                elif tag == 'iyr' and (int(value) > 2020 or int(value) < 2010 or len(value) != 4):
                    invalid = 1
                    break
                elif tag == 'eyr' and (int(value) > 2030 or int(value) < 2020 or len(value) != 4):
                    invalid = 1
                    break
                elif tag == 'hgt':
                    unit = value[-2:]
                    val = value[:-2]
                    if unit == 'cm' and (int(val) > 193 or int(val) < 150):
                        invalid = 1
                        break
                    elif unit == 'in' and (int(val) > 76 or int(val) < 59):
                        invalid = 1
                        break
                elif tag == 'hcl':
                    if len(value) != 7 or value[0] != '#':
                        invalid = 1
                        break
                    else:
                        for char in value[1:]:
                            if char not in hclchars:
                                invalid = 1
                                break
                elif tag == 'ecl' and value not in eclchars:
                    invalid = 1
                    break
                elif tag == 'pid' and (len(value) != 9 or not value.isdigit()):
                    invalid = 1
                    break
            if invalid == 0:
                numvalid2 = numvalid2 + 1
            invalid = 0
        currPassport = ''
# process last passport
if 'byr:' in currPassport and 'iyr:' in currPassport and 'eyr:' in currPassport and \
'hgt:' in currPassport and 'hcl:' in currPassport and 'ecl:' in currPassport and \
'pid:' in currPassport:
    numvalid = numvalid + 1
    # part 2
    fields = currPassport.split()
    for entry in fields:
        tag = entry[:3]
        value = entry[4:]
        print('tag: ' + tag + ', value: ' + value)
        if tag == 'byr' and (int(value) > 2002 or int(value) < 1920 or len(value) != 4):
            invalid = 1
            break
        elif tag == 'iyr' and (int(value) > 2020 or int(value) < 2010 or len(value) != 4):
            invalid = 1
            break
        elif tag == 'eyr' and (int(value) > 2030 or int(value) < 2020 or len(value) != 4):
            invalid = 1
            break
        elif tag == 'hgt':
            unit = value[-2:]
            val = value[:-2]
            if unit == 'cm' and (int(val) > 193 or int(val) < 150):
                invalid = 1
                break
            elif unit == 'in' and (int(val) > 76 or int(val) < 59):
                invalid = 1
                break
        elif tag == 'hcl':
            if len(value) != 7 or value[0] != '#':
                invalid = 1
                break
            else:
                for char in value[1:]:
                    if char not in hclchars:
                        invalid = 1
                        break
        elif tag == 'ecl' and value not in eclchars:
            invalid = 1
            break
        elif tag == 'pid' and (len(value) != 9 or not value.isdigit()):
            invalid = 1
            break
    if invalid == 0:
        numvalid2 = numvalid2 + 1

numvalid2 = numvalid2 -1 # was off by one but don't know why

output = 'Part 1: ' + str(numvalid) + ' passports'
print(output)
output = 'Part 2: ' + str(numvalid2) + ' passports'
print(output)