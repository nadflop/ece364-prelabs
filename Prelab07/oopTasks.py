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
        if level not in Level:
            raise TypeError("The arguent must be an instance of the 'Level' Enum")
        self.level = level.name

    def __str__(self):
        return f"{self.ID}, {self.firstName} {self.lastName}, {self.level}"

#component class
class Component:
    def __init__(self, ID, ctype, price):
        self.ID = ID
        self._validateCtype(ctype)
        self.price = price

    def _validateCtype(self, cype):
        if cype not in ComponentType:
            raise TypeError("The arguent must be an instance of the 'ComponentType' Enum")
        self.ctype = cype.name

    def __str__(self):
        price = format(self.price, ".2f")
        return f"{self.ctype}, {self.ID}, ${price}"

    def __hash__(self):
        return hash(self.ID)

#circuit class
class Circuit(Component):
    def __init__(self, ID, components):
        self.ID = ID
        self.components = components
        if components == set():
            raise TypeError("Components must not be an empty set")
        price = 0
        for items in components:
            if self._validateComponent(items) == False:
                raise TypeError("Set must be an instance of the Component class")
            price += items.price
            self.cost = price
            #add the component set to components variables
    def __len__(self):
        return len(self.components)

    def _validateComponent(self, component):
        return isinstance(component,Component)

    def __add__(self, components):
        self.addComponent(components)
        return self

    def addComponent(self, someComponent):
        if self._validateComponent(someComponent) == True:
            self.components.add(someComponent)
            newCost = round(self.cost + someComponent.price,2)
            self.cost = newCost
        else:
            return

    def __sub__(self, components):
        self.subComponent(components)
        return self

    def subComponent(self, someComponent):
        if self._validateComponent(someComponent) == True:
            self.components.remove(someComponent)
            newCost = round(self.cost - someComponent.price,2)
            self.cost = newCost
        else:
            raise TypeError("Component must be an instance of Component class")
            return

    def __str__(self):
        R = ComponentType.Resistor
        C = ComponentType.Capacitor
        I = ComponentType.Inductor
        T = ComponentType.Transistor
        RCount = self.getByType(R)
        CCount = self.getByType(C)
        TCount = self.getByType(T)
        ICount = self.getByType(I)
        cost = format(self.cost, ".2f")
        return f"{self.ID}: (R={format(len(RCount),'02d')}, C={format(len(CCount),'02d')}, " \
               f"I={format(len(ICount),'02d')}, T={format(len(TCount),'02d')}), Cost = ${cost}"
    
    def getByType(self, compType):
        element = set()
        if compType not in ComponentType:
            raise TypeError("must pass in a member of ComponentType")
        for items in self.components:
            if items.ctype == compType.name:
                element.add(items)
        return element

#project class
class Project:
    def __init__(self, ID, participants, cost):
        self.ID = ID


    def _validateCtype(self, ctype):
        if ctype not in ComponentType.__members__.keys():
            raise TypeError("The arguent must be an instance of the 'ComponentType' Enum")
        self.ctype = ctype

    def __str__(self):
        return f"{self.ID}: ({format(len(RCount),'02d')} Circuits, {format(len(CCount),'02d')} Participants, " \
               f"Cost = ${cost}"

#capstone class
class Capstone:
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
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    level = Level.Freshman
    student = Student('15487-79431', 'John', 'Smith', level)
    print(student)
    c1 = ComponentType.Resistor
    c2 = ComponentType.Capacitor
    c3 = ComponentType.Inductor
    c4 = ComponentType.Transistor
    comp1 = Component('TAZ-349', c4, 1.10)
    comp2 = Component('CUI-043', c2, 0.15)
    comp3 = Component('QLS-943', c3, 0.36)
    comp4 = Component('ORW-143', c1, 0.15)
    comp5 = Component('TFL-784', c4, 1.55)
    comp6 = Component('BTP-574', c4, 1.72)
    comp7 = Component('CPF-254', c2, 1.01)
    comp8 = Component('RCW-957', c1, 0.74)
    comp9 = Component('NKT-617', c4, 2.29)
    comp10 = Component('TDP-854', c4, 0.22)
    #components = {comp1,comp2,comp3,comp4,comp5,comp6,comp7,comp8,comp9}
    comp = {comp9,comp10}
    circuit = Circuit('10-0-55', comp)
    print(circuit)