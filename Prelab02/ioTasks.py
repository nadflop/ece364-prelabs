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

def getMaxDifference(symbol: str) -> str:
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        #raw = f.readline()#read and return line in files seperately
        rawData = f.readlines()

    maxDiff = 0

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

def getGainPercent(symbol: str):
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        raw = f.readline()  # read and return line in files seperately

def getVolumeSum(symbol: str, date1, date2):
    if date1 >= date2:
        return None

    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        raw = f.readline()  # read and return line in files seperately

def getBestGain(date):
    pass

def getAveragePrice(symbol: str, year):
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        raw = f.readline()  # read and return line in files seperately

def getCountOver(symbol: str, price):
    filename = symbol.__add__('.dat')
    DataText = os.path.join(DataPath, filename)
    with open(DataText) as f:
        raw = f.readline()  # read and return line in files seperately

# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
   getMaxDifference('AAPL')