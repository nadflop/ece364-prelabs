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

def reportData(key): #get mapping between ID and report
    from collections import namedtuple
    virus = namedtuple("virus", ["user", "ID", "unit"])

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
        userID = str(temp[-1])

        if key == 0: #just get data between reportID and userID
            if userID in reportDict:
                reportDict[userID] += reportID
            else:
                reportDict[userID] = reportID
        if key == 1: #get reportID, userID, virus names and amount
            virusList = []
            for item in data[4:]:
                [t,v,u] = item.split()
                virusList.append(virus(userID,v,u))
            reportDict[reportID[0]] = virusList

    return reportDict

def virusData(key): #get mapping between virus name, ID and price
    from collections import namedtuple
    virus = namedtuple("virus", ["ID", "price"])

    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'viruses.dat')
    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    virusDict = { }

    for element in data[2:]:
        while '|' in element:
            element.remove('|')
        if key == 0: #name as key
            virusDict[element[0]] = virus(element[1], element[2].replace('$', ''))
        elif key == 1: #ID as key
            virusDict[element[1]] = virus(element[0], element[2].replace('$', ''))

    return virusDict
#------------------------------problem 1--------------------------------------------------------------------------------
def getTechWork(techName: str) -> dict:
    DataFolder = os.path.join(DataPath, 'reports')
    techDict = techData(0) #get dict between name and ID
    reportDict = reportData(0)
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
#-----------------------------------------problem 2---------------------------------------------------------------------
def getStrainConsumption(virusName: str)-> dict:
    DataFolder = os.path.join(DataPath, 'reports')
    reportDict = reportData(0)
    virusDict = virusData(1)
    techDict = techData(1)
    resultDict = { }

    for userID in reportDict.keys():
        for filename in reportDict[userID]:
            DataFile = os.path.join(DataFolder, 'report_' + filename + '.dat')
            with open(DataFile) as f:
                data = [line.strip() for line in f.read().splitlines()]

            for line in data[4:]:
                [t,v,u] = str(line).split()

                if virusName in virusDict[v].ID:
                    if userID in resultDict:
                        resultDict[techDict.get(userID)] += int(u)
                    else:
                        resultDict[techDict.get(userID)] = int(u)

    return resultDict
#------------------------------------------------problem 3--------------------------------------------------------------
def getTechSpending()-> dict:
    #round value by 2 decimals
    pass
#----------------------------------------------problem 4----------------------------------------------------------------
def getStrainCost()-> dict:
    #round value by 2 decimals
    pass
#-------------------------------------------------problem 5-------------------------------------------------------------
def getAbsentTech()-> set:
    pass
#--------------------------------------------------problem 6------------------------------------------------------------
def getUnusedStrains()-> set:
    pass


if __name__ == "__main__":
    getTechWork('Adams, Keith')
    getStrainConsumption('Hepadnaviridae')