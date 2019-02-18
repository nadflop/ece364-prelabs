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
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab02")
#------------------------------------------------------------------problem 1--------------------------------------------
def getMaxDifference(symbol: str) -> str:
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText, "r") as f:
        #raw = f.readline()#read and return line in files seperately
        rawData = f.readlines()

    maxDiff = 0

    #rawData[2:]
    for i in range(2, len(rawData)):
        newData = str(rawData[i]).split(',')
        p = newData[5].split('\n')
        z = p.pop() #to remove the '\n'
        z = p.pop() #get the list as string
        diff = float(newData[4]) - float(str(z))
        if round(diff, 4) > maxDiff:
            maxDiff = diff
            date = str(newData[0])

    return date
#-------------------------------------------problem 2-------------------------------------------------------------------
def getGainPercent(symbol: str):
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    try:
        with open(DataText, "r") as f:
            rawData = f.readlines()  # read and return line in files seperately
    except:
        raise ValueError("Symbol not found")

#    maxDiff = 0
    day = 0

    #rawData[2:]
    for i in range(2, len(rawData)):
        newData = str(rawData[i]).split(',')
        diff = float(newData[1]) - float(newData[3])
        if round(diff, 4) > 0:
#            maxDiff = diff
            day = day + 1

    percent = round((day/(len(rawData) - 2)) * 100, 4)

    return percent
#-------------------------------------------------------problem 3-------------------------------------------------------
def getVolumeSum(symbol: str, date1: str, date2: str) -> int:
    if date1 >= date2:
        return None

    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    for i in range(2, len(rawData)):
        newData = str(rawData[i]).split(',')
        if date1 in newData[0]:
            sum1 = newData[2]
        if date2 in newData[0]:
            sum2 = newData[2]

    sumVolume = float(sum1) + float(sum2)
    total = int(round(sumVolume))

    return total
#----------------------------------------------------problem 4----------------------------------------------------------
def getBestGain(date: str):
    flname = [ ]
    for root, dirs, files in os.walk(DataPath):
        for filename in files:
            flname.append(filename)

    maxGain = 0

    for item in flname:
        DataText = os.path.join(DataPath, item)
        with open(DataText) as f:
            rawData = f.readlines()  # read and return line in files seperately
        for i in range(2, len(rawData)):
            newData = str(rawData[i]).split(',')
            if date in newData[0]:
                closeVal = float(newData[1])
                openVal = float(newData[3])
                gain = (closeVal - openVal) / openVal * 100
                if gain > maxGain:
                    maxGain = round(gain, 4)

    return maxGain
#-----------------------------------------------------------------problem 5---------------------------------------------
def getAveragePrice(symbol: str, year: int):
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    avg = 0

    for i in range(2, len(rawData)):
        newData = str(rawData[i]).split(',')
        date = newData[0].split('/')
        if str(year) in date[0]:
            closeVal = float(newData[1])
            openVal = float(newData[3])
            val = (closeVal + openVal) / 2
            avg = avg + val

    return round(avg, 4)
#-----------------------------------------------------------problem 6---------------------------------------------------
def getCountOver(symbol: str, price: float):
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    days = 0
#    tmp = [ ]

    for i in range(2, len(rawData)):
        tmp = [ ]
        newData = str(rawData[i]).split(',')
        p = newData[5].split('\n')
        z = p.pop()  # to remove the '\n'
        highPrice = float(p.pop())  # get the list as string
        for j in range(1, len(newData) - 1):
            if j != 2:
                tmp.append(float(newData[j]))
        tmp.append(highPrice)
        if all(val >= price for val in tmp):
            days = days + 1

    return days

# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    print(getGainPercent("asdf"))
    ...