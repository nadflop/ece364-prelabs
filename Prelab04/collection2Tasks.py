#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/1
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab04")

def getTechWork(techName: str) -> dict:
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'technicians.dat')  # open projects file
    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    pass

def getStrainConsumption(virusName: str)-> dict:
    DataFile = os.path.join(DataPath, 'reports')
    flname = []
    for root, dirs, files in os.walk(DataFile):
        for filename in files:
            flname.append(filename)

    reportDict = { }

    for item in flname:
        CircFile = os.path.join(DataFile, item)
        with open(CircFile) as f:
            data = [line.strip() for line in f.read().splitlines()]
        t = item.replace('report_', '')
        s = t.replace('.dat', '')
        reportDict[s] = data[2:data.index('Components:')- 1]

    pass

def getTechSpending()-> dict:
    #round value by 2 decimals
    pass

def getStrainCost()-> dict:
    #round value by 2 decimals
    pass

def getAbsentTech()-> set:
    pass

def getUnusedStrains()-> set:
    pass


if __name__ == "__main__":
    ...