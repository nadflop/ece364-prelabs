#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 1/11
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab01")
DataText = os.path.join(DataPath, 'sequence.txt')

#-------------------------problem 1----------------------
def find(pattern: str) -> str:
    #open file to get the sequence
    with open(DataText) as f:
        sequence = f.read()
    f.close()
    temp = [ ] #temporarily stores the list of testable sequence
    result = [ ] #the list of patterns in the sequence
    patSize = len(pattern) #size of the pattern
    seqSize = len(sequence) #size of the sequence
    #check if the size of pattern is bigger than sequence
    if patSize > seqSize:
        return
    #if not, proceed to find the pattern
    for x in range(seqSize - patSize + 1):
        temp = [ ]
        for y in range(patSize):
            if pattern[y] == sequence[x]:
                temp.append(sequence[x])
                x = x + 1 #make sure we iterate to the next list
            elif pattern[y] == 'X':
                temp.append(sequence[x])
                x = x + 1
            else:
                break
            if y == patSize - 1: #since index starts with 0, need to minus 1
                result.append(''.join(temp))
                break

    return result

#---------------problem 2----------------------------
def getStreakProduct(sequence: str, maxSize: int, product: int) -> str:
    seqSize = len(sequence)
    minSize = 2 #the size of the sub-sequences (min: 2, max: maxSize)
    p = 1
    temp = [ ]
    result = [ ]

    if seqSize < minSize:  # check if it meets the requirement
        return result

    for x in range(seqSize):
        temp = [ ]
        p = 1
        for y in range(maxSize):
            p = p * int(sequence[x])
            mod = product % p
            if mod == 0:
                temp.append(sequence[x])
                if x in range(seqSize - 1):
                    x = x + 1
            else:
                if x in range(seqSize - 1):
                    x = x + 1
                    break
            if y == maxSize and p == product:
                result.append(''.join(temp))
                break
            elif len(temp) >= minSize and p == product:
                result.append(''.join(temp))
                break

    return result

#-------------------problem 3--------------------------------
def writePyramids(filePath: str, baseSize: int, count: int, char: str):
    #generate line n for a single pyramid
    #generate a single pyramid, then use it to generate the rest
    #combine the pyramids in a list
    #write the list to the target file
    if baseSize % 2 == 0: #if its even number, return
        return
    line = [ ]

    for i in range(0, baseSize):

        for j in range(0, i):


#--------------------problem 4-----------------------------
def getStreaks(sequence: str, letters: str) -> list:
    seqSize = len(sequence)
    letSize = len(letters)
    temp = [ ]
    result = [ ]
    ptr = 0
    j = 0
    i = 0

    while i < seqSize:
        temp = [ ]
        j = 0
        while j < letSize:
            if sequence[i] == letters[j]:
                for k in range(i, seqSize):
                    if sequence[k] == sequence[i]:
                        temp.append(sequence[k])
                        ptr = ptr + 1
                    else:
                        break
                result.append(''.join(temp))
                j = letSize
            else:
                j = j + 1
        if ptr != 0:
            i = i + ptr
            ptr = 0
        else:
            i = i + 1

    return result
#---------------------------problem 5------------------------
def findNames(nameList: str, part: str, name: str) -> str:
    result = [ ]
    if part == 'L':
        for i in range(len(nameList)):
            newList = nameList[i].split()
            if str(newList[1]).lower() == name.lower():
                result.append(nameList[i])
    elif part == 'F':
        for i in range(len(nameList)):
            newList = nameList[i].split()
            if str(newList[0]).lower() == name.lower():
                result.append(nameList[i])
    elif part == 'FL':
        for i in range(len(nameList)):
            newList = nameList[i].split()
            if str(newList[0]).lower() == name.lower():
                result.append(nameList[i])
            elif str(newList[1]).lower() == name.lower():
                result.append(nameList[i])

    return result
#-------------------------problem 6---------------------
def convertToBoolean(num: int, size: int) -> str:
    binary = [ ]
    booleanList = [ ]

    if type(num) != int:
        return binary

    binary = bin(num).replace("0b", "")
    print(binary)
    diff = size - len(binary)
    print(diff)

    for i in range(0, len(binary)):
        if binary[i] == '1':
            booleanList.append('True')
        elif binary[i] == '0':
            booleanList.append('False')
        else:
            break

    if diff > 0:
        for j in range(diff):
            booleanList.reverse()
            booleanList.append('False')
            booleanList.reverse()

    return(booleanList)
#---------------------------problem 7----------------------------
def convertToInteger(boolList: list) -> int:
    if len(boolList) == 0:
        return

    if type(boolList) != list:
        return

    for item in boolList:
        if type(item) != bool:
            return

    binary = [ ]

    for i in range(len(boolList)):
        if boolList[i] == False:
            binary.append('0')
        elif boolList[i] == True:
            binary.append('1')

    result = int(''.join(binary), 2)
    return result
# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    r = getStreaks(sequence, "PAZ")
    print(r)