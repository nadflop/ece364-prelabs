#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/1
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from collections import namedtuple
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab04")
#----------------create a dictionary between the tech ID and tech Name--------------------------------------------------
def techData(key: int):
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'technicians.dat')
    techDict = { }

    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]
    if key == 0: #name as key, ID as value
        for item in data[2:]:
            name = item[0] + ' ' + item[1]
            techDict[name] = item[-1]
    elif key == 1:#ID as key, name as value
        for item in data[2:]:
            name = item[0] + ' ' + item[1]
            techDict[item[-1]] = name

    return techDict
#-------------------------create dictionary of report ID, user ID, viruses used and its units---------------------------
def reportData(key: int):
    DataFile = os.path.join(DataPath, 'reports')
    virus = namedtuple("virus", ["user", "ID", "unit"])
    flname = []
    reportDict = { }
    for root, dirs, files in os.walk(DataFile):
        for filename in files:
            flname.append(filename)

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
#---------------------------dictionary between virus name, ID and price-------------------------------------------------
def virusData(key):
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'viruses.dat')
    virus = namedtuple("virus", ["ID", "price"])
    virusDict = {}

    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

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
    techDict = techData(0) #key: techName, value: techID
    reportDict = reportData(1) #key: reportID, value: (userID, virusID, unit)
    virusDict = virusData(1) #key: virusID, value: (virusName,price)
    resultDict = { }

    for element in reportDict.values():
        for v in element:
            if str(v[0]) == techDict[techName]:
                if virusDict[v[1]].ID in resultDict:
                   resultDict[virusDict[v[1]].ID] += int(v[2])
                else:
                    resultDict[virusDict[v[1]].ID] = int(v[2])

    return resultDict
#-----------------------------------------problem 2---------------------------------------------------------------------
def getStrainConsumption(virusName: str)-> dict:
    reportDict = reportData(1)#key: report ID, value: (user, virusID, unit)
    virusDict = virusData(0) #key: virusName, value: (virusID, price)
    techDict = techData(1) #key: techID, value: techName
    resultDict = { }
    virusID = virusDict[virusName].ID

    for element in reportDict.values():
        for v in element:
            if virusID == v[1]:
                userID = v[0]
                if techDict.get(userID) in resultDict:
                    resultDict[techDict.get(userID)] += int(v[2])
                else:
                    resultDict[techDict.get(userID)] = int(v[2])

    return resultDict
#------------------------------------------------problem 3--------------------------------------------------------------
def getTechSpending()-> dict: #round value by 2 decimals
    reportDict = reportData(1)  # key: report ID, value: (user, virusID, unit)
    virusDict = virusData(1)  # key: virusID, value: (virusName, price)
    techDict = techData(1)  # key: techID, value: techName
    resultDict = {}

    for element in reportDict.values():
        for v in element:
            userID = v[0]
            if techDict.get(userID) in resultDict:
                value = round(float(resultDict[techDict.get(userID)]) + float(virusDict[v[1]].price) * int(v[2]),2)
                resultDict[techDict.get(userID)] = value
            else:
                resultDict[techDict.get(userID)] = round(float(virusDict[v[1]].price) * int(v[2]), 2)

    return resultDict
#----------------------------------------------problem 4----------------------------------------------------------------
def getStrainCost()-> dict:
    reportDict = reportData(1)  # key: report ID, value: (user, virusID, unit)
    virusDict = virusData(1)  # key: virusID, value: (virusName, price)
    techDict = techData(1)  # key: techID, value: techName
    resultDict = { }

    for virusID in virusDict.keys():
        for element in reportDict.values():
            for v in element:
                if virusID == v[1]:
                    if virusDict[v[1]].ID in resultDict:
                        value = round(float(resultDict[virusDict[v[1]].ID]) + float(virusDict[v[1]].price) * int(v[2]), 2)
                        resultDict[virusDict[v[1]].ID] = value
                    else:
                        resultDict[virusDict[v[1]].ID] = round(float(virusDict[v[1]].price) * int(v[2]), 2)

    return resultDict
#-------------------------------------------------problem 5-------------------------------------------------------------
def getAbsentTech()-> set:
    techID = [*reportData(0)] #get the list of techID involved in experiments
    techDict = techData(1)  # key: techID, value: techName
    t1 = set(techDict.keys()) #set of all techID
    t2 = set(techID) #set of techID involved in experiments
    temp = t1.difference(t2)
    result = set()

    if len(temp) != 0:
        for item in temp:
            result.add(techDict.get(item))

    return result
#--------------------------------------------------problem 6------------------------------------------------------------
def getUnusedStrains()-> set:
    virusName = [*getStrainCost()] #virus used in the experiment
    virusDict = virusData(0)  # key: virusName, value: (virusID, price)
    v1 = set(virusDict.keys())  # set of all virusName
    v2 = set(virusName)  # set of virusName involved in experiments
    result = set()
    result = v1.difference(v2)

    return result
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ...
