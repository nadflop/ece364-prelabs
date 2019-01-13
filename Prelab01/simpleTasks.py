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
def getStreakProduct(sequence: str, maxSize, product):
    pass

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
    result = find('9XX3')
    print(result)