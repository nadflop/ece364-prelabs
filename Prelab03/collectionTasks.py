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
        circStudMap[s] = data[2:data.index('Components:')]

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
    result = set()
    s1 = [ ]

    circuit = projMap.get(projectID) #get all list of circuits build in proj

    if len(circuit) == 0:
        raise ValueError("The projectID doesn't seems to exists")

    typeMap = compToTypeMap() #mapping between componentID to its type
    s1 = typeMap.get(componentSymbol)  # get all the components for that type

    circMap = circToCompMap()#mapping between circuitID and the components

    for item in circuit:
        for k in circMap.get(item): #components
            for j in s1:
                if k == j:
                    result.add(k)
                    '''
                    if k in result:  # make sure the item is distinct
                        del result[result.index(k)]
                    else:
                        result.append(k)
                    '''
    return len(result)
#-------------------------------------------------problem 2-------------------------------------------------------------
def getComponentCountByStudent(studentName: str, componentSymbol: str) -> int:
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
        if k.First == F and k.Last == L:
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
    circMap = circToCompMap()
    circuit1 = set()
    circuit2 = set()

    circuit1 = set(projMap[projectID1])  # get all list of circuits build in proj
    circuit2 = set(projMap[projectID2])  # get all list of circuits build in proj

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
    i = 0

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
            if ',' in element:
                n = str(element).split()
                L = n[0].rstrip(',')
                F = n[1]
            else:
                n = str(element).split()
                F = n[0]
                L = n[0]
            if F == k.First and L == k.Last:
                    studentID.append(nameMap[k])

    for j in studentID:
        for k in circMap.keys():
            for item in circMap[k]:
                if item == j:
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


if __name__ == "__main__":
    r1 = getComponentCountByProject("08EDAB1A-743D-4B62-9446-2F1C5824A756", "R")
    print("[Q{}] ans match? {}".format(1, r1 == 99))

    r2 = getComponentCountByStudent("Young, Frank", "I")
    print("[Q{}] ans match? {}".format(2, r2 == 14))

    r3 = getParticipationByStudent("Young, Frank")
    test_r3 = {'90BE0D09-1438-414A-A38B-8309A49C02EF', 'FE647EE2-2EBD-4837-83F0-256C377365FE',
               '0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A', '177EBF38-1C20-497B-A2EF-EC1880FEFDF9',
               'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05', '082D6241-40EE-432E-A635-65EA8AA374B6',
               '7C376AFE-6D98-4E50-B29C-71FBF6260B2D', '4C5B295B-58E1-4CFB-80DF-88938B9A6300',
               '075A54E6-530B-4533-A2E4-A15226BE588C', '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9',
               'D230BAC0-249C-410F-84E4-41F9EDBFCB20', '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287',
               '6CCCA5F3-3008-46FF-A779-2D2F872DAF82'}
    print("[Q{}] ans match? {}".format(3, r3 == test_r3))

    r4 = getParticipationByProject("08EDAB1A-743D-4B62-9446-2F1C5824A756")
    test_r4 = {'Watson, Martin', 'Henderson, Christopher', 'Davis, Douglas', 'Gonzalez, Kimberly', 'Lowe, Karen',
               'Green, Roy', 'Richardson, George', 'Wright, Eric', 'Thomas, Mark', 'Turner, Theresa', 'Kelly, Joyce',
               'Moore, John', 'Brooks, Carol', 'Reed, Bobby', 'Coleman, Lori', 'Morgan, Edward', 'Bryant, Evelyn',
               'Brown, Robert', 'Garcia, Martha', 'Anderson, Debra', 'Perry, Marie', 'Allen, Amanda', 'Gray, Tammy',
               'Lewis, William', 'Cook, Margaret', 'Bennett, Nancy', 'Carter, Sarah', 'Hughes, James',
               'Bell, Kathryn', 'Evans, Johnny', 'Thompson, Michelle', 'Cooper, Kelly', 'Torres, Betty',
               'Morris, Heather', 'Powell, Gregory', 'Hill, Jose', 'Hall, Beverly', 'Lee, Julie', 'Simmons, Cynthia',
               'Stewart, Earl', 'Ward, Sandra', 'Jackson, Doris', 'Wood, Kevin', 'Jones, Stephanie',
               'Roberts, Teresa', 'Martinez, David', 'Phillips, Brenda', 'Russell, Scott', 'Gonzales, Arthur',
               'Williams, Mary', 'Walker, Terry', 'Price, Dorothy', 'Clark, Joe', 'King, Carolyn', 'Ross, Frances',
               'White, Diana', 'Campbell, Eugene', 'Foster, Benjamin', 'Taylor, Brian', 'Scott, Michael',
               'Wilson, Howard', 'Smith, Jimmy', 'Harris, Anne'}
    print("[Q{}] ans match? {}".format(4, r4 == test_r4))

    r5 = getCostOfProjects()
    test_r5 = {'56B13184-D087-48DB-9CBA-84B40FE17CC5': 355.36, '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9': 350.93,
               '17A946D3-A1B0-4335-8808-8594D9FBD62C': 295.25, 'DE06228A-0544-4543-9055-A39D19DEDFA4': 375.37,
               '082D6241-40EE-432E-A635-65EA8AA374B6': 245.46, 'D230BAC0-249C-410F-84E4-41F9EDBFCB20': 235.24,
               '08EDAB1A-743D-4B62-9446-2F1C5824A756': 376.4, '7C376AFE-6D98-4E50-B29C-71FBF6260B2D': 249.63,
               '66FA081D-D1AA-4306-8650-9C39429CCDAB': 256.63, '90BE0D09-1438-414A-A38B-8309A49C02EF': 335.16,
               '96CC6F98-B44B-4FEB-A06B-390432C1F6EA': 268.48, '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA': 394.44,
               '6CCCA5F3-3008-46FF-A779-2D2F872DAF82': 233.6, 'FE647EE2-2EBD-4837-83F0-256C377365FE': 213.73,
               '8E56417E-0D81-4F43-8137-F1F7AA005654': 262.39, 'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05': 428.72,
               '177EBF38-1C20-497B-A2EF-EC1880FEFDF9': 334.98, '77A1A82E-749E-43BF-B3BF-3E70F087F808': 369.48,
               'D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371': 241.42, '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287': 370.65,
               '2E7649C2-574A-496A-850B-F15190031E11': 304.08, '075A54E6-530B-4533-A2E4-A15226BE588C': 358.84,
               '32B9E998-97C3-4D5A-8005-C9685A08196F': 400.34, '8C71F259-ECA8-4267-A8B3-6CAD6451D4CC': 325.13,
               '83383848-1D69-40D4-A360-817FB22769ED': 367.49, '4C5B295B-58E1-4CFB-80DF-88938B9A6300': 388.81,
               '0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A': 292.63, 'B9C94766-617A-4168-B2AA-44FFE8323E32': 231.96}
    print("[Q{}] ans match? {}".format(5, r5 == test_r5))

    r6 = getProjectByComponent({"ZHT-034", "CWQ-065", "NOC-324"})
    test_r6 = {'90BE0D09-1438-414A-A38B-8309A49C02EF', 'D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371',
               '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9', '32B9E998-97C3-4D5A-8005-C9685A08196F',
               '96CC6F98-B44B-4FEB-A06B-390432C1F6EA', '2E7649C2-574A-496A-850B-F15190031E11',
               'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05', 'DE06228A-0544-4543-9055-A39D19DEDFA4',
               '082D6241-40EE-432E-A635-65EA8AA374B6', '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287',
               '0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A', '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA',
               'FE647EE2-2EBD-4837-83F0-256C377365FE', '7C376AFE-6D98-4E50-B29C-71FBF6260B2D',
               '83383848-1D69-40D4-A360-817FB22769ED', 'B9C94766-617A-4168-B2AA-44FFE8323E32',
               '77A1A82E-749E-43BF-B3BF-3E70F087F808', '66FA081D-D1AA-4306-8650-9C39429CCDAB'}
    print("[Q{}] ans match? {}".format(6, r6 == test_r6))

    r7 = getCommonByProject("08EDAB1A-743D-4B62-9446-2F1C5824A756", "082D6241-40EE-432E-A635-65EA8AA374B6")
    test_r7 = ['ACT-109', 'ACU-407', 'AGC-216', 'ATI-589', 'AVL-897', 'BLT-317', 'CBU-096', 'CCT-418', 'CFI-435',
               'CFY-502', 'CIS-470', 'CIW-539', 'CKN-960', 'CLG-567', 'CLJ-178', 'CLQ-971', 'CLW-864', 'CNM-019',
               'CQL-174', 'CRU-015', 'CTM-765', 'CUH-362', 'CUP-407', 'DCB-178', 'DTX-021', 'ELQ-692', 'ERK-824',
               'EVC-461', 'FCI-290', 'FUR-815', 'GTV-294', 'GVR-469', 'GVR-698', 'HFT-317', 'HLL-239', 'HLM-864',
               'HOR-267', 'HRI-734', 'HUC-107', 'IBC-258', 'ILT-213', 'JLE-057', 'JNL-870', 'JSC-743', 'JTM-187',
               'KLF-473', 'KPT-041', 'KSR-430', 'KUR-213', 'LAD-263', 'LAI-791', 'LAW-453', 'LCB-902', 'LCD-472',
               'LIT-491', 'LJR-923', 'LLR-943', 'LOK-793', 'LRK-875', 'LRY-825', 'LRZ-426', 'LVE-357', 'LWY-204',
               'MAT-263', 'MBR-643', 'MGC-590', 'MLJ-635', 'NCD-108', 'NUR-482', 'OLW-497', 'OPL-704', 'OUT-239',
               'PTC-309', 'PTI-732', 'QIC-567', 'QXT-230', 'RCL-035', 'RCW-957', 'RFR-136', 'RFU-406', 'RHN-426',
               'RIK-619', 'RKP-916', 'RLL-937', 'RMY-042', 'RNW-027', 'ROJ-198', 'RPK-296', 'RSB-276', 'RSH-743',
               'RTN-652', 'RWR-683', 'SJL-465', 'TAQ-610', 'TAU-413', 'TCH-815', 'TED-890', 'TIR-328', 'TLP-793',
               'TLR-058', 'TOM-325', 'TQJ-016', 'TSC-032', 'TSW-590', 'TTC-861', 'TVC-129', 'UMT-238', 'UNL-746',
               'URK-539', 'UTA-912', 'UTH-014', 'VFL-589', 'VNR-234', 'VSR-074', 'VTL-437', 'WHT-451', 'XRJ-639',
               'XRY-260', 'XRZ-943', 'YKC-827', 'YLF-462', 'YWT-432', 'ZTN-927', 'ZWR-028']

    print("[Q{}] ans match? {}".format(7, r7 == test_r7))

    r8 = getComponentReport({"ZHT-034", "CWQ-065", "NOC-324"})
    test_r8 = {'CWQ-065': 0, 'NOC-324': 21, 'ZHT-034': 0}
    print("[Q{}] ans match? {}".format(8, r8 == test_r8))

    r9 = getCircuitByStudent({"Adams, Keith", "Young, Frank "})
    test_r9 = {'60-9-98', '75-9-18', '51-8-46', '30-8-14', '11-1-44', '48-2-28', '19-9-86'}
    print("[Q{}] ans match? {}".format(9, r9 == test_r9))

    r10 = getCircuitByComponent({"ZHT-034", "CWQ-065", "NOC-324"})
    test_r10 = {'15-5-65', '65-2-28', '35-6-63', '41-0-60', '24-6-74', '65-0-76'}
    print("[Q{}] ans match? {}".format(10, r10 == test_r10))
