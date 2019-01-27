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

#-----------------------------------problem 1--------------------------------------------
def getComponentCountByProject(projectID: str, componentSymbol: str) -> int:
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'projects.dat') #open projects file
    with open(DataText) as f:
        rawData = f.readlines()

    compMap = {'R': "resistors.dat",
               'I': "inductors.dat",
               'C': "capacitors.dat",
               'T': "transistors.dat"}
    circuit = [ ]
    uniqueComp = [ ]

    #find if the project ID exists in the projects.dat file
    for item in rawData:
        oldData = str(item).strip()
        newData = str(oldData).split()
        for item in newData:
            if projectID == str(item):
                circuit.append(newData[0])#take the circuit ID
    #raise an error if it doesn't exists
    if len(circuit) == 0:
        raise ValueError("The projectID doesn't seems to exists")
    #from the circuit ID, find the file in the circuits folder
    for item in circuit:
        IDFile = os.path.join(DataPath, 'circuits')
        filename = 'circuit_' + str(item) + '.dat';
        IDText = os.path.join(IDFile, filename)  # open projects file
        with open(IDText) as f:
            data = [line.rstrip('\n') for line in f.read().splitlines()]

        compList = data[data.index('Components:')+2:]#get the components ID

        CompText = os.path.join(DataFile, compMap[componentSymbol.upper()])#check dictionary to know which folder to open
        with open(CompText) as f:
            compData = [line.strip() for line in f.read().splitlines()]

        for item1 in compList:
            item1 = item1.strip()
            for item2 in compData:
                test = item2.split()
                #print(item1)
                if item1 in test[0].strip():
                    if item1 in uniqueComp:#make sure the item is distinct
                        del uniqueComp[uniqueComp.index(item1)]
                    else:
                        uniqueComp.append(item1)

    return len(uniqueComp)

def getComponentByStudent(studentName, componentSymbol):
    pass

def getParticipationByStudent(studentName):
    pass

def getParticipationByProject(projectID):
    pass

def getCostOfProjects():
    pass

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
    num = getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'c')
    print(num)
    