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

def techData(key: int):
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'technicians.dat')
    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    techDict = { }

    if key == 0: #name as key, ID as value
        for item in data[2:]:
            name = item[0] + ' ' + item[1]
            techDict[name] = item[-1]
    elif key == 1:#ID as key, name as value
        for item in data[2:]:
            name = item[0] + ' ' + item[1]
            techDict[item[-1]] = name

    return techDict
    '''
    from collections import namedtuple
    virus = namedtuple("virus", ["name", "unit"])

    for element in data[4:]:
        [t, v, u] = element.split()
        virusData = virus(v, u)
        virusList.append(virusData)
    '''
def reportData(): #get mapping between ID and report
    DataFile = os.path.join(DataPath, 'reports')
    flname = []

    for root, dirs, files in os.walk(DataFile):
        for filename in files:
            flname.append(filename)

    reportDict = { }

    for item in flname:
        reportID = [ ]
        CircFile = os.path.join(DataFile, item)
        with open(CircFile) as f:
            data = [line.strip() for line in f.read().splitlines()]
        t = item.replace('report_', '')
        reportID.append(t.replace('.dat', '')) #report ID

        temp = str(data[0]).split() #get techID
        userID = temp[-1]

        if userID in reportDict:
            reportDict[userID] += reportID
        else:
            reportDict[userID] = reportID

    return reportDict


def createDict(key, value)-> dict:
    myDict = { }

    for item in key:
        for element in value:
            myDict[item] = element

    return myDict

def getTechWork(techName: str) -> dict:
    DataFolder = os.path.join(DataPath, 'reports')
    techDict = techData(0) #get dict between name and ID
    reportDict = reportData()
    resultDict = { }

    for filename in reportDict[techDict[techName]]:
        DataFile = os.path.join(DataFolder, 'report_' + filename + '.dat')
        with open(DataFile) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for line in data[4:]:
            [t,v,u] = str(line).split()

            if v in resultDict:
                resultDict[v] += int(u)
            else:
                resultDict[v] = int(u)

    return resultDict

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
    getTechWork('Adams, Keith')
    reportData()