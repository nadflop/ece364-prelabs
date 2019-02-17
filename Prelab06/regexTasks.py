#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/15
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
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
#if ID and state are present, ID first then state
#if have everything = excepted
#if have name but no other = rejected
#if have name and one or two additional fields, partially complete
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
    pass

def getEmployeesWithoutIDs()-> list:
    pass

def getEmployeesWithPhones()-> dict:
    #key: employee name, value: phone number
    pass

def getEmployeesWithStates()-> dict:
    #key: employee name, value: state name
    pass

def getCompleteEntries()-> dict:
    #key: employee name,
    # value: tuple(ID, phone number, state of residence)
    pass


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