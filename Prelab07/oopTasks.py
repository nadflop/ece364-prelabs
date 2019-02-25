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
#-----------------------------------------------------------------------------------------------------------------------
class ComponentType(Enum):
    Resistor = 1
    Capacitor = 2
    Inductor = 3
    Transistor = 4
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------
#circuit class
class Circuit:

    def __init__(self, ID, components):
        self.ID = ID
        if components == set():
            raise TypeError("Components must not be an empty set")
        price = 0
        temp = set()
        for items in components:
            if self._validateComponent(items) == False:
                raise TypeError("Set must be an instance of the Component class")
            price += items.price
            self.cost = price
            temp.add(items)
            self.components = temp

    def _validateComponent(self, component):
        return isinstance(component,Component)

    def __contains__(self, someComponent):
        if self._validateComponent(someComponent) == False:
            raise TypeError("Component must be an instance of Component class")
        return hasattr(self,someComponent)

    def __add__(self, components):
        if components not in self.components:
            self.addComponent(components)
        return self

    def addComponent(self, someComponent):
        if self._validateComponent(someComponent) == True:
            self.components.add(someComponent)
            newCost = round(self.cost + someComponent.price,2)
            self.cost = newCost

    def __sub__(self, components):
        if components in self.components:
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

    def __lt__(self, another_circuit):
        return self.cost < another_circuit.cost

    def __gt__(self, another_circuit):
        return self.cost > another_circuit.cost

    def __eq__(self, another_circuit):
        return self.cost == another_circuit.cost

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
#-----------------------------------------------------------------------------------------------------------------------
#project class
class Project:
    def __init__(self, ID, participants, circuits, cost):
        self.ID = ID
        self.participants = []
        self.circuits = []
        if participants == []:
            raise ValueError("Participants list must not be an empty set")
        if circuits == []:
            raise ValueError("Circuit List must not be empty")
        for students in participants:
            if self._validateParticipant(students) == False:
                raise TypeError("Participant must be an instance of the Student class")
            self.participants.append(students)
        price = 0
        for circ in circuits:
            if self._validateCircuit(circ) == False:
                raise TypeError("Circuit must be an instance of the Circuit class")
            self.circuits.append(circ)
            price += circ.cost
        self.cost = price

    def _validateParticipant(self, stud):
        return isinstance(stud, Student)

    def _validateCircuit(self, circ):
        return isinstance(circ, Circuit)

    def _validateComponent(self, component):
        return isinstance(component,Component)

    def __contains__(self, something):
        if (self._validateCircuit(something) and self._validateComponent(something) and self._validateParticipant(something)) == False:
            raise ValueError("Item passed is neither a Student, Component or Circuit instance")
        return hasattr(self,something)

    def __add__(self, circuits):
        if circuits not in self.circuits:
            self.addCircuit(circuits)
        return self

    def addCircuit(self, someCircuit):
        if self._validateCircuit(someCircuit) == True:
            self.circuits.append(someCircuit)
            newCost = round(self.cost + someCircuit.cost, 2)
            self.cost = newCost
        else:
            raise TypeError("Circuit must be an instance of Circuit class")

    def __sub__(self, circuits):
        if circuits in self.circuits:
            self.subCircuit(circuits)
        return self

    def subCircuit(self, someCircuit):
        if self._validateComponent(someCircuit) == True:
            self.circuits.remove(someCircuit)
            newCost = round(self.cost - someCircuit.cost, 2)
            self.cost = newCost
        else:
            raise TypeError("Circuit must be an instance of Circuit class")

    def __getitem__(self, item):
        try:
            for element in self.circuits:
                if item == element.ID:
                    return element
        except:
            raise KeyError("Circuit ID doesn't exists in the project")

    def __str__(self):
        cost = format(self.cost, ".2f")
        return f"{self.ID}: ({format(len(self.circuits),'02d')} Circuits, {format(len(self.participants),'02d')} Participants), " \
               f"Cost = ${cost}"
#-----------------------------------------------------------------------------------------------------------------------
#capstone class
class Capstone(Project):
    def __init__(self, *args):
        if len(args) > 1:
            ID = args[0]
            participants = args[1]
            circuits = args[2]
            super().__init__(ID,participants,circuits,0)
        else:
            self = args
        self._validateLevel(self.participants)
    def _validateLevel(self,someParticipants):
        for student in someParticipants:
            if student.level is not Level.Senior.name:
                raise ValueError("some participating students are not seniors")
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ...