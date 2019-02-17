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

#PART 1
def getUrlParts(url: str)-> tuple :
    #'http://[Base adress]/[controller]/[action]?[querystring]
    pattern = re.search('(?P<address>[\w.-]+)\/(?P<controller>[\w.-]+)\/(?P<action>[\w.-]+)', url)
    addrs = pattern["address"]
    ctrl = pattern["controller"]
    act = pattern["action"]
    parts = (addrs,ctrl,act)

    return parts

def getQueryParameters(url: str)-> list:
    #'http://[Base adress]/[controller]/[action]?[querystring]
    pattern = re.findall('\?([\w.-=_&]+)', url)
    result = []
    temp = re.findall(r'\b[\w.-=_]+[^{&}\W]\b', str(pattern),re.I)
    for item in temp:
        (a,b) = re.findall(r'\b[\w.-]+[^{=}\W]\b', item, re.I)
        result.append((a,b))
    return result

def getSpecial(sentence:str, letter:str)-> list:
    pattern = re.findall(r'\b[{i}]\w*[^{i}\W]\b|\b[^{i}\W]\w*[{i}]\b'.format(i = letter), sentence, re.I)

    return pattern

def getRealMAC(sentence:str)-> str :
    #if not found, return None
    pattern = re.findall(r'\b[0-9a-fA-F:0-9a-fA-F]{17}|\b[0-9a-fA-F-0-9a-fA-F]{17}', sentence, re.I)
    if len(pattern) == 0:
        return None

    return pattern

#PART 2
#name, ID, phone, state
def getRejectedEntries()-> list:
    rejected = []
    DataFile = os.path.join(DataPath, 'Employees.txt')
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.findall(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}',lines,re.I)
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

    return rejected
def getEmployeesWithIDs()-> dict:
    #key: employee name, value: ID
    resultDict = {}
    DataFile = os.path.join(DataPath, 'Employees.txt')
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.search(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}',lines,re.I)
        if id != None:
            n = str(name["first"]+' '+name["last"])
            resultDict[n] = str(UUID(id.group()))

    return resultDict

def getEmployeesWithoutIDs()-> list:
    result = []
    DataFile = os.path.join(DataPath, 'Employees.txt')
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.search(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}',lines,re.I)
        if id == None:
            n = str(name["first"]+' '+name["last"])
            result.append(n)

    return result

def getEmployeesWithPhones()-> dict:
    #key: employee name, value: phone number
    resultDict = {}
    DataFile = os.path.join(DataPath, 'Employees.txt')
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

def getEmployeesWithStates()-> dict:
    #key: employee name, value: state name
    resultDict = {}
    DataFile = os.path.join(DataPath, 'Employees.txt')
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

def getCompleteEntries()-> dict:
    #key: employee name,
    # value: tuple(ID, phone number, state of residence)
    complete = {}
    DataFile = os.path.join(DataPath, 'Employees.txt')
    with open(DataFile, "r") as f:
        data = f.readlines()

    for lines in data:
        name = re.search(r'(?P<last>[a-zA-Z]+),\s(?P<first>[a-zA-Z]+)', lines)
        if name == None:
            name = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+),', lines)
        id = re.search(r'\b[(0-9)(a-fA-F)]{8}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{4}-\b[(0-9)(a-fA-F)]{12}',lines,re.I)
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


if __name__ == "__main__":
    from pprint import pprint as pp
    url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    pp(getUrlParts(url))
    url2 = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
    pp(getQueryParameters(url2))
    s = "The TART program runs on Tuesdays and Thursdays, but it doesn not start until next week"
    pp(getSpecial(s,"t"))
    pp(getRealMAC('hello 58:1C:0A:6E:39:4D eh kau pehal 3F:0B:55:A7:3E:99'))
    pp(getRejectedEntries())
    pp(getEmployeesWithIDs())
    pp(getEmployeesWithoutIDs())
    pp(getEmployeesWithPhones())
    pp(getEmployeesWithStates())
    pp(getCompleteEntries())