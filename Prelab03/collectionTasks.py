#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 1/24
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab03")

#helper functions

def projToCircMap(): #mapping for ProjectID to CircuitID
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'projects.dat')  # open projects file
    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    projMap = { }
    circuitID = [ ]
    key = 'A'

    for item in data[2:]:
        item.reverse()
        if key != item[0]:
            circuitID = [ ]
            key = item[0]
            circuitID.append(item[1])
            projMap[key] = circuitID
        else:
            circuitID.append(item[1])
            projMap[key] = circuitID

    return projMap

def circToCompMap():#mapping for circuitID to componentID
    DataFile = os.path.join(DataPath, 'circuits')
    flname = [ ]
    for root, dirs, files in os.walk(DataFile):
        for filename in files:
            flname.append(filename)

    circMap = { }

    for item in flname:
        CircFile = os.path.join(DataFile, item)
        with open(CircFile) as f:
            data = [line.strip() for line in f.read().splitlines()]
        t = item.replace('circuit_', '')
        s = t.replace('.dat', '')
        circMap[s] = data[data.index('Components:') + 2:]

    return circMap

def compToTypeMap():#mapping between type of component and their IDs
    typeMap = {'R': "resistors.dat",
               'I': "inductors.dat",
               'C': "capacitors.dat",
               'T': "transistors.dat"}

    compMap = { }
    c = [ ]

    DataFile = os.path.join(DataPath, 'maps')
    for v in typeMap.values():
        DataText = os.path.join(DataFile, v)  # open the associated component file
        with open(DataText) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for k in typeMap.keys():
            c = [ ]
            if typeMap[k] == v:
                for item in data[3:]:
                    item = item.split()
                    c.append(item[0])
                    compMap[k] = c

    return compMap

def compToCostMap():#mapping between cost of component and their IDs
    typeMap = {'R': "resistors.dat",
               'I': "inductors.dat",
               'C': "capacitors.dat",
               'T': "transistors.dat"}

    costMap = { }
    c = [ ]

    DataFile = os.path.join(DataPath, 'maps')
    for v in typeMap.values():
        DataText = os.path.join(DataFile, v)  # open the associated component file
        with open(DataText) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for k in typeMap.keys():
            c = [ ]
            if typeMap[k] == v:
                for item in data[3:]:
                    item = item.split()
                    costMap[item[0]] = item[1].replace('$', '')

    return costMap






#-----------------------------------problem 1--------------------------------------------
def getComponentCountByProject(projectID: str, componentSymbol: str) -> int:
    projMap = projToCircMap()
    circuit = [ ]
    result = [ ]
    s1 = [ ]
    projMap = projToCircMap()
    for k in projMap.keys():    #find if the project ID exists
        if projectID == str(k):
            circuit = projMap[k] #get all list of circuits build in proj

    if len(circuit) == 0:
        raise ValueError("The projectID doesn't seems to exists")

    typeMap = compToTypeMap() #mapping between componentID to its type
    for k in typeMap.keys():
        if componentSymbol == k:
            s1 = typeMap[k]  # get all the components for that type

    circMap = circToCompMap()#mapping between circuitID and the components
    for item in circuit:
        for k in circMap.keys():
            if item == k:
                components = circMap[k] #get all the component used in the circuit
                for i in components:
                    for j in s1:
                        if i == j:
                            if i in result:  # make sure the item is distinct
                                del result[result.index(i)]
                            else:
                                result.append(i)

    return len(result)
#-------------------------------------------------problem 2-------------------------------------------------------------
def getComponentByStudent(studentName: str, componentSymbol: str) -> int:
    from collections import namedtuple
    student = namedtuple("Student", ["First", "Last", "ID"])

    '''
    flname = [ ]
    for root, dirs, files in os.walk(DataFile):
        for filename in files:
            flname.append(filename)

    for item in flname:
        DataText = os.path.join(DataFile, item)
        with open(DataText) as f:
            rawData = f.readlines()  # read and return line in files seperately
    '''
#-------------------------------------problem 3------------------------------------------------------------------------
def getParticipationByStudent(studentName):
    pass

def getParticipationByProject(projectID):
    pass
#------------------------------------problem 5--------------------------------------------------------------------------
def getCostOfProjects() -> dict:
    projMap = projToCircMap()
    circMap = circToCompMap()
    compMap = compToCostMap()
    print(circMap)
    print(compMap)
    circVal = { }
    projVal = { }
    cost = 0

    for key in circMap.keys():
        cost = 0
        for item in circMap[key]:
            for k in compMap.keys():
                if item == k:
                    cost = cost + float(compMap[k])
        circVal[key] = cost

    for key in projMap.keys():
        total = 0
        for item in projMap[key]:
            for k in circVal.keys():
                if item == k:
                    total = total + circVal[k]
        projVal[key] = round(total, 2)

    return projVal


def getProjectByComponent(componentIDs):
    pass

def getCommonByProject(projectID1, projectID2):
    pass

def getComponentReport(componentIDs):
    pass

def getCircuitByStudent(studentNames):
    pass

def getCircuitByComponent(componentIDs):
    pass



# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    #projToCompMap()
    compToCostMap()
    num = getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'R')
    print(num)
    getComponentByStudent('Julia Butler', 'I')
    r = getCostOfProjects()
    print(r)