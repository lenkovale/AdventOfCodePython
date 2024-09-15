def calibrate(document):
    number = 0
    for line in document.splitlines():
            a = ''
            b = ''
            for i in range(len(line)):
                if a == '':
                    a = findTextDigits(line, i)
                    if(line[i].isdigit()):
                            a = int(line[i])
                if b == '':
                    b = findTextDigits(line, len(line)-1-i)                         
                    if(line[len(line)-1-i].isdigit()):
                        b = int(line[len(line)-1-i])
                if (b != '' and a != ''):
                     break
            number += (a * 10 + b)          
    return number

def findTextDigits(line, index):
    digits = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for dig in digits.keys():
        finded = line.find(dig, index)
        if (finded == index):
            return digits[dig]
    return ''

