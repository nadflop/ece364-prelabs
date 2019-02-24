#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/24
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from enum import Enum
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class Level(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior = 4

class ComponentType(Enum):
    Resistor = 1
    Capacitor = 2
    Inductor = 3
    Transistor = 4

#student class
class Student:
    def __init__(self, ID, firstName, lastName, level):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self._validateLevel(level)

    def _validateLevel(self, level):
        if level not in Level.__members__.keys():
            raise TypeError("The arguent must be an instance of the 'Level' Enum")
        self.level = level

    def __str__(self):
        return f"{self.ID}, {self.firstName} {self.lastName}, {self.level}"

#component class
class Component:
    def __init__(self, ID, ctype, price):
        self.ID = ID
        self._validateCtype(ctype)
        self.price = format(price, ".2f")

    def _validateCtype(self, ctype):
        if ctype not in ComponentType.__members__.keys():
            raise TypeError("The arguent must be an instance of the 'ComponentType' Enum")
        self.ctype = ctype

    def __str__(self):
        return f"{self.ctype}, {self.ID}, ${self.price}"

    def __hash__(self):
        return hash(self.ID)

#circuit class
class Circuit:
    def __init__(self, ID, components, cost):
        self.ID = ID
        self._validateComponent(components)

    def _validateComponents(self, components):
        if components == set():
            raise TypeError("Components can't be an empty set")
        for ctype in components:
            if ctype not in Component.ID:
                raise TypeError("The arguent must be an instance of the 'ComponentType' Enum")
            self.components.add(ctype)

    #def __str__(self):

        #return f"{self.ID}: (R={}, C={}, I={}, T={}), Cost = ${self.cost}"


    def getByType(self, components):
        for ctype in components:
            if ctype not in ComponentType.__members__.keys():
                raise TypeError("The arguent must be an instance of the 'ComponentType' Enum")
            self.components.add(ctype)


#project class
#capstone class
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    student = Student('15487-79431', 'John', 'Smith', 'Freshman')
    print(student)
    component = Component('REW-321', 'Resistor', 1.40)
    print(component)