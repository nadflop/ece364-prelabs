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
##----------------------------------------------mapping for ProjectID to CircuitID--------------------------------------
def projToCircMap():
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
#-------------------------------------mapping for circuitID to componentID----------------------------------------------
def circToCompMap():
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
#----------------------------------mapping between circuit ID and student-----------------------------------------------
def circToStudent():
    DataFile = os.path.join(DataPath, 'circuits')
    flname = [ ]
    for root, dirs, files in os.walk(DataFile):
        for filename in files:
            flname.append(filename)

    circStudMap = { }

    for item in flname:
        CircFile = os.path.join(DataFile, item)
        with open(CircFile) as f:
            data = [line.strip() for line in f.read().splitlines()]
        t = item.replace('circuit_', '')
        s = t.replace('.dat', '')
        circStudMap[s] = data[2:data.index('Components:')- 1]

    return circStudMap
#-------------------------------------------mapping between circuit ID and student--------------------------------------
def compToTypeMap():
    typeMap = {'R': "resistors.dat",
               'I': "inductors.dat",
               'C': "capacitors.dat",
               'T': "transistors.dat"}

    compMap = { }

    DataFile = os.path.join(DataPath, 'maps')
    for filename in typeMap.values():
        DataText = os.path.join(DataFile, filename)  # open the associated component file
        with open(DataText) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for symbol in typeMap.keys():
            component = [ ]
            if typeMap[symbol] == filename:
                for item in data[3:]:
                    item = item.split()
                    component.append(item[0])
                compMap[symbol] = component

    return compMap
#----------------------------mapping between cost of component and their IDs--------------------------------------------
def compToCostMap():
    typeMap = {'R': "resistors.dat",
               'I': "inductors.dat",
               'C': "capacitors.dat",
               'T': "transistors.dat"}

    costMap = { }

    DataFile = os.path.join(DataPath, 'maps')
    for filename in typeMap.values():
        DataText = os.path.join(DataFile, filename)  # open the associated component file
        with open(DataText) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for keys in typeMap.keys():
            if typeMap[keys] == filename:
                for item in data[3:]:
                    item = item.split()
                    costMap[item[0]] = item[1].replace('$', '')

    return costMap
#----------------------------------------mapping between student name to its ID-----------------------------------------
def studentToIDMap():
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'students.dat')
    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    studMap = { }

    for item in data[2:]:
        name = item[0] + ' ' + item[1]
        studMap[name] = item[-1]

    return studMap
#----------------------------------------mapping between student ID to its name-----------------------------------------
def IDToStud():
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'students.dat')
    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    studMap = { }

    for item in data[2:]:
        name = item[0] + ' ' + item[1]
        studMap[item[-1]] = name

    return studMap
#----------------------------------------mapping between projID to student ID-------------------------------------------
def projToStudID():
    projMap = projToCircMap() #get the mapping between projID and circuit ID
    circMap = circToStudent() #get the mapping between circuit ID and student ID
    s1 = [ ] #create an empty set
    projStudMap = { }

    #do mapping between projID and studentID
    for projID in projMap.keys():
        s1 = [ ]
        for circuit in projMap[projID]:
            for component in circMap.get(circuit):
                s1.append(component)
        projStudMap[projID] = s1

    return projStudMap
#-----------------------------------problem 1---------------------------------------------------------------------------
def getComponentCountByProject(projectID: str, componentSymbol: str) -> int:
    projMap = projToCircMap()
    circuit = [ ]
    result = set()
    s1 = [ ]

    circuit = projMap.get(projectID) #get all list of circuits build in proj

    if len(circuit) == 0:
        raise ValueError("The projectID doesn't seems to exists")

    typeMap = compToTypeMap() #mapping between componentID to its type
    s1 = typeMap.get(componentSymbol)  # get all the components for that type

    circMap = circToCompMap()#mapping between circuitID and the components

    for item in circuit:
        for components in circMap.get(item): #components
            for element in s1:
                if components == element:
                    result.add(components)

    return len(result)
#-------------------------------------------------problem 2-------------------------------------------------------------
def getComponentCountByStudent(studentName: str, componentSymbol: str) -> int:
    studMap = studentToIDMap()

    ID = studMap[studentName]
    s1 = set()

    if len(ID) == 0:
        raise ValueError("The student name passed doesn't exist")

    DataFile = os.path.join(DataPath, 'circuits')
    flname = [ ]
    for root, dirs, files in os.walk(DataFile):
        for filename in files:
            flname.append(filename)

    components = [ ]

    for item in flname:
        CircFile = os.path.join(DataFile, item)
        with open(CircFile) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for d in data:
            if d == ID:
                components.append(data[data.index('Components:') + 2:])

    typeMap = compToTypeMap()  # mapping between componentID to its type
    for k in typeMap.keys():
        if componentSymbol == k:
            s1 = typeMap[k]

    result = [ ]

    if len(components) == 0: #student didn't participate in any project
        return 0
    else:
        for item in components:
            for k in item:
                for element in s1:
                    if k == element:
                        if k in result:  # make sure the item is distinct
                            del result[result.index(k)]
                        else:
                            result.append(k)

    return len(result)
#-------------------------------------problem 3------------------------------------------------------------------------
def getParticipationByStudent(studentName: str) -> set:
    studMap = studentToIDMap()
    ID = studMap[studentName]
    if len(ID) == 0:
        raise ValueError("The student name passed doesn't exist")

    projMap = projToStudID()
    result = set()

    for k in projMap.keys():
        for element in projMap[k]:
            if element == ID:
                result.add(k)#add the proj ID into the set

    return result
#-------------------------------------problem 4-------------------------------------------------------------------------
def getParticipationByProject(projectID):
    projMap = projToStudID() #mapping between projID and studentID
    studID = IDToStud() #mapping between student ID and name
    result = set()

    try:
        student = projMap.get(projectID)
    except:
        raise ValueError("Project ID doesn't exists")

    for element in student:
        name  = studID[element]
        result.add(name)

    return result
#------------------------------------problem 5--------------------------------------------------------------------------
def getCostOfProjects() -> dict:
    projMap = projToCircMap()
    circMap = circToCompMap()
    compMap = compToCostMap()
    circVal = { }
    projVal = { }

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
#-------------------------------------problem 6-------------------------------------------------------------------------
def getProjectByComponent(componentIDs: set) -> set:
    result = set()
    projMap = projToCircMap()
    circMap = circToCompMap() #get the mapping between circuits and component
    component = list(componentIDs)
    circID = set()

    #get the circuit ID for the components in the list
    for keys in circMap.keys():
        for element in component:
            for item in circMap[keys]:
                if element == item:
                    circID.add(keys)

    circuit = list(circID)

    for keys in projMap.keys():
        for element in circuit:
            for item in projMap[keys]:
                if element == item:
                    result.add(keys)

    return result
#-------------------------------------problem 7-------------------------------------------------------------------------
def getCommonByProject(projectID1, projectID2):
    projMap = projToCircMap()
    circMap = circToCompMap()
    circuit1 = [ ]
    circuit2 = [ ]
    circuit1 = projMap[projectID1]  # get all list of circuits build in proj
    circuit2 = projMap[projectID2]  # get all list of circuits build in proj

    if len(circuit1) == 0:
        raise ValueError("The projectID1 doesn't seems to exists")
    if len(circuit2) == 0:
        raise ValueError("The projectID2 doesn't seems to exists")

    comp1 = set()
    comp2 = set()
    for elements in circuit1:
        for components in circMap.get(elements):
            comp1.add(components)
    for elements in circuit2:
        for components in circMap.get(elements):
            comp2.add(components)

    comp3 = comp1 & comp2
    result = list(comp3)
    result.sort(key=str)

    return result
#------------------------------------problem 8--------------------------------------------------------------------------
def getComponentReport(componentIDs: set)-> dict:
    projMap = projToCircMap()
    circMap = circToCompMap() #get the mapping between circuits and component
    circID = { }
    temp = { }
    comp = [ ]
    val = 0

    #for items in componentIDs:
    for projID in projMap.keys():
        comp = [ ]
        for circuit in projMap[projID]:
            for component in circMap.get(circuit):
                comp.append(component)
        temp[projID] = comp

    #loop through the componentIDs first, then find matching comp in circuit
    for element in componentIDs:
        val = 0
        for keys in temp.keys():
            for item in temp[keys]:
                if element == item:
                    val = val + 1 #keep track the number of occurences
            circID[element] = val

    return circID
#-----------------------------------problem 9---------------------------------------------------------------------------
def getCircuitByStudent(studentNames: set) -> set:
    names = list(studentNames)
    circMap = circToStudent() #get mapping between circuitID and student ID
    studentID = [ ] #get mapping between studentID and name
    nameMap = studentToIDMap() #get mapping between student name and ID
    result = set()

    #find all the student IDs
    for element in names:
        for k in nameMap.keys():
            if element == k:
                studentID.append(nameMap[k])

    for ID in studentID:
        for circuit in circMap.keys():
            for element in circMap[circuit]:
                if element == ID:
                    result.add(circuit)

    return result
#-----------------------------------problem 10--------------------------------------------------------------------------
def getCircuitByComponent(componentIDs: set)-> set:
    circMap = circToCompMap()
    comp = list(componentIDs)
    circID = set()

    for item in comp:
        for k in circMap.keys():
            for element in circMap[k]:
                if element == item:
                    circID.add(k)

    return circID


if __name__ == "__main__":
    ...