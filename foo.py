stringone = "2 av 3"
stringtwo = "1"
stringthree = "4"
stringfour = "11"

def calculate_floor(hej):

    if(len(hej) > 1):
        numberone = hej.split('av')[0]
        numberone = int(numberone)

        if(numberone < 2):
            return 0
        else:
            return 1
    elif(int(hej) < 2):
        return 0
    else:
        return 1

'''
print(calculate_floor(stringone))
print(calculate_floor(stringtwo))
print(calculate_floor(stringthree))
print(calculate_floor(stringfour))
'''

strtest = "Tranebergsvägen 91 - Accepterat pris!"
strtest2 = "Tranebergsvägen 107, vån 3/3"

def stripStr(teststring):
    print(teststring.replace('-', ',').split(',')[0])

stripStr(strtest)
stripStr(strtest2)
