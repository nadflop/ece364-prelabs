#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/15
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
from uuid import UUID
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab06")
DataFile = os.path.join(DataPath, 'Employees.txt')
#PART 1
#-------------------------------------------------problem 1-------------------------------------------------------------
def getUrlParts(url: str)-> tuple :
    #'http://[Base adress]/[controller]/[action]?[querystring]
    pattern = re.search('(?P<address>[\w.-]+)\/(?P<controller>[\w.-]+)\/(?P<action>[\w.-]+)', url)
    addrs = pattern["address"]
    ctrl = pattern["controller"]
    act = pattern["action"]
    parts = (addrs,ctrl,act)

    return parts
#-------------------------------------------------problem 2-------------------------------------------------------------
def getQueryParameters(url: str)-> list:
    #'http://[Base adress]/[controller]/[action]?[querystring]
    pattern = re.findall('\?([\w.-=_&]+)', url)
    result = []
    temp = re.findall(r'\b[\w.-=_]+[^{&}\W]\b', str(pattern),re.I)
    for item in temp:
        (a,b) = re.findall(r'\b[\w.-]+[^{=}\W]\b', item, re.I)
        result.append((a,b))
    return result
#-------------------------------------------------problem 3-------------------------------------------------------------
def getSpecial(sentence:str, letter:str)-> list:
    pattern = re.findall(r'\b[{i}]\w*[^{i}\W]\b|\b[^{i}\W]\w*[{i}]\b'.format(i = letter), sentence, re.I)

    return pattern
#-------------------------------------------------problem 4-------------------------------------------------------------
def getRealMAC(sentence:str)-> str :
    #if not found, return None
    pattern = re.findall(r'\b[0-9a-fA-F:0-9a-fA-F]{17}|\b[0-9a-fA-F-0-9a-fA-F]{17}', sentence, re.I)
    if len(pattern) == 0:
        return None

    return pattern

#PART 2
#-------------------------------------------------problem 5-------------------------------------------------------------
def getRejectedEntries()-> list:
    rejected = []
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.findall(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}|\b[(0-9)(a-fA-F)]{32}',lines,re.I)
        no = re.findall(r'\b[\d]{10}|\b[\d-]{12}|\([^()]+\)\s\d+-\d+', lines)
        state = re.findall(r'([(a-zA-Z)\s]+\Z)',lines)
        if len(state) > 0:
            temp = re.findall(r'[(a-zA-Z)\s]+',str(state),re.MULTILINE)#seperate the \n
            if len(temp) > 1:
                state = [temp[0]]
            else:
                state = []
        if len(id) == 0 and len(no) == 0 and len(state) == 0:
            rejected.append(name["first"]+ ' '+name["last"])

    r = sorted(rejected,key=str)
    return r
#-------------------------------------------------problem 6-------------------------------------------------------------
def getEmployeesWithIDs()-> dict:
    #key: employee name, value: ID
    resultDict = {}

    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.search(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}|\b[(0-9)(a-fA-F)]{32}',lines,re.I)
        if id != None:
            n = str(name["first"]+' '+name["last"])
            resultDict[n] = str(UUID(id.group()))

    return resultDict
#-------------------------------------------------problem 7-------------------------------------------------------------
def getEmployeesWithoutIDs()-> list:
    result = []
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.search(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}|\b[(0-9)(a-fA-F)]{32}',lines,re.I)
        if id == None:
            n = str(name["first"]+' '+name["last"])
            result.append(n)

    r = sorted(result,key=str)

    return r
#-------------------------------------------------problem 8-------------------------------------------------------------
def getEmployeesWithPhones()-> dict:
    #key: employee name, value: phone number
    resultDict = {}
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        no = re.search(r'\b[\d]{10}|\b[\d-]{12}|\([^()]+\)\s\d+-\d+', lines)
        if no != None:
            n = str(name["first"]+' '+name["last"])
            if len(no.group()) == 14:
                resultDict[n] = no.group()
            elif len(no.group()) == 12:
                part = re.search(r'(?P<one>[\d]+[^-])-(?P<two>[\d]+[^-])-(?P<three>[\d]+)', no.group())
                nmbr = '(' + part["one"] + ')' + ' ' + part["two"] + '-' + part["three"]
                resultDict[n] = nmbr
            elif len(no.group()) == 10:
                part = re.search(r'(?P<one>[\d]{3})(?P<two>[\d]{3})(?P<three>[\d]{4})', no.group())
                nmbr = '(' + part["one"] + ')' + ' ' + part["two"] + '-' + part["three"]
                resultDict[n] = nmbr

    return resultDict
#-------------------------------------------------problem 9-------------------------------------------------------------
def getEmployeesWithStates()-> dict:
    #key: employee name, value: state name
    resultDict = {}
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        state = re.search(r'([(a-zA-Z)\s]+\Z)', lines)
        if state != None:
            temp = re.search(r'[(a-zA-Z)\s][^\n]+', str(state.group()), re.MULTILINE)  # seperate the \n
            if temp != None:
                state = temp.group()
            else:
                state = None
        if state != None:
            n = str(name["first"]+' '+name["last"])
            resultDict[n] = state

    return resultDict
#-------------------------------------------------problem 10------------------------------------------------------------
def getCompleteEntries()-> dict:
    #key: employee name,
    # value: tuple(ID, phone number, state of residence)
    complete = {}
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.search(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}|\b[(0-9)(a-fA-F)]{32}',lines,re.I)
        no = re.search(r'\b[\d]{10}|\b[\d-]{12}|\([^()]+\)\s\d+-\d+', lines)
        state = re.search(r'([(a-zA-Z)\s]+\Z)', lines)
        if state != None:
            temp = re.search(r'[(a-zA-Z)\s][^\n]+', str(state.group()), re.MULTILINE)  # seperate the \n
            if temp != None:
                state = temp.group()
            else:
                state = None

        if no != None:
            if len(no.group()) == 14:
                nmbr = no.group()
            elif len(no.group()) == 12:
                part = re.search(r'(?P<one>[\d]+[^-])-(?P<two>[\d]+[^-])-(?P<three>[\d]+)', no.group())
                nmbr = '(' + part["one"] + ')' + ' ' + part["two"] + '-' + part["three"]
            elif len(no.group()) == 10:
                part = re.search(r'(?P<one>[\d]{3})(?P<two>[\d]{3})(?P<three>[\d]{4})', no.group())
                nmbr = '(' + part["one"] + ')' + ' ' + part["two"] + '-' + part["three"]

        if id != None and len(nmbr) != 0 and state != None:
            n = name["first"]+ ' '+name["last"]
            element = (str(UUID(id.group())), nmbr, state)
            complete[n] = element

    return complete
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ...