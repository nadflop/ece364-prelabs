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
def writePyramids(filePath, baseSize, count, char):
    pass

def getStreaks(sequence, letters):
    pass

def findNames(nameList, part, name):
    pass

def convertToBoolean(num, size):
    pass

def convertToInteger(boolList):
    pass



def functionName1(a:float, b:float) ->float:
    pass
def functionName2(c:str, d:str) ->int:
    pass
# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    result = getStreakProduct('54789654321687984', 5, 288)
    print(result)