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
        circStudMap[s] = data[2:data.index('Components:') - 1]

    return circStudMap
#-------------------------------------------mapping between circuit ID and student--------------------------------------
def compToTypeMap():
    typeMap = {'R': "resistors.dat",
               'I': "inductors.dat",
               'C': "capacitors.dat",
               'T': "transistors.dat"}

    compMap = { }

    DataFile = os.path.join(DataPath, 'maps')
    for v in typeMap.values():
        DataText = os.path.join(DataFile, v)  # open the associated component file
        with open(DataText) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for k in typeMap.keys():
            component = [ ]
            if typeMap[k] == v:
                for item in data[3:]:
                    item = item.split()
                    component.append(item[0])
                    compMap[k] = component

    return compMap
#----------------------------mapping between cost of component and their IDs--------------------------------------------
def compToCostMap():
    typeMap = {'R': "resistors.dat",
               'I': "inductors.dat",
               'C': "capacitors.dat",
               'T': "transistors.dat"}

    costMap = { }

    DataFile = os.path.join(DataPath, 'maps')
    for v in typeMap.values():
        DataText = os.path.join(DataFile, v)  # open the associated component file
        with open(DataText) as f:
            data = [line.strip() for line in f.read().splitlines()]
        for k in typeMap.keys():
            if typeMap[k] == v:
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

    from collections import namedtuple
    Student = namedtuple("Student", ["First", "Last"])

    studMap = { }

    for item in data[2:]:
        studMap[Student(item[1], item[0].rstrip(','))] = item[-1]

    return studMap
#----------------------------------------mapping between student ID to its name-----------------------------------------
def IDToStud():
    DataFile = os.path.join(DataPath, 'maps')
    DataText = os.path.join(DataFile, 'students.dat')
    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    from collections import namedtuple
    Student = namedtuple("Student", ["First", "Last"])

    studMap = { }

    for item in data[2:]:
        studMap[item[-1]] = Student(item[1], item[0].rstrip(','))

    return studMap
#----------------------------------------mapping between projID to student ID-------------------------------------------
def projToStudID():
    projMap = projToCircMap() #get the mapping between projID and circuit ID
    circMap = circToStudent() #get the mapping between circuit ID and student ID
    s1 = set() #create an empty set
    projStudMap = { }

    #do mapping between projID and studentID
    for keys in projMap.keys():
        for item in projMap[keys]:
            s1 = set()
            for k in circMap.keys():
                if item == k: #if its the same circuit ID
                    s2 = set(circMap[k])
                    s1= s1 | s2
        projStudMap[keys] = s1

    return projStudMap
#-----------------------------------problem 1---------------------------------------------------------------------------
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
    studMap = studentToIDMap()
    if ',' in studentName:
        name = studentName.split()
        L = name[0].rstrip(',')
        F = name[1]
    else:
        [F, L] = studentName.split()

    ID = ''
    s1 = set()

    for k in studMap.keys():
        if [k.First, k.Last] == [F, L]:
            ID = studMap[k]
        if k.First == F:
            if k.Last == L:
                ID = studMap[k]

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
    if ',' in studentName:
        name = studentName.split()
        L = name[0].rstrip(',')
        F = name[1]
    else:
        [F, L] = studentName.split()

    ID = ''

    for k in studMap.keys():
        if [k.First, k.Last] == [F, L]:
            ID = studMap[k]
        if k.First == F:
            if k.Last == L:
                ID = studMap[k]

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

    for k in projMap.keys():  # find if the project ID exists
        if projectID == str(k):
            for element in projMap[k]:
                for item in studID.keys():
                    if element == item:
                        name = studID[item].First + ' ' + studID[item].Last
                        result.add(name) #add the name to the set

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
    circuit1 = set()
    circuit2 = set()

    for k in projMap.keys():  # find if the project ID exists
        if projectID1 == str(k):
            circuit1 = set(projMap[k])  # get all list of circuits build in proj
        if projectID2 == str(k):
            circuit2 = set(projMap[k])  # get all list of circuits build in proj

    if len(circuit1) == 0:
        raise ValueError("The projectID1 doesn't seems to exists")
    if len(circuit2) == 0:
        raise ValueError("The projectID2 doesn't seems to exists")

    circuit3 = circuit1 & circuit2

    return list(circuit3)
#------------------------------------problem 8--------------------------------------------------------------------------
def getComponentReport(componentIDs: set)-> dict:
    circMap = circToCompMap() #get the mapping between circuits and component
    component = list(componentIDs)
    circID = { }
    val = 0

    #loop through the componentIDs first, then find matching comp in circuit
    for element in component:
        val = 0
        for keys in circMap.keys():
            for item in circMap[keys]:
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
            if ',' in names:
                n = str(element).split()
                L = n[0].rstrip(',')
                F = n[1]
            else:
                n = str(element).split()
                F = n[0]
                L = n[0]
            if F == k.First:
                if L == k.Last:
                    studentID.append(nameMap[k])

    for element in studentID:
        for k in circMap.keys():
            for item in circMap[k]:
                if item == element:
                    result.add(k)

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


# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    p = getComponentByStudent('Russell, Scott', 'T')
    print(p)