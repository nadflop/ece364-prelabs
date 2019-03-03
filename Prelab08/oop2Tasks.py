#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 3/2
#######################################################
import os  # List of  module  import  statements
import sys  # Each  one on a line
from enum import Enum
import copy
import math
from functools import total_ordering
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class Datum:
    #defines a point R" Space
    _storage = tuple()

    def __init__(self, *args):
        for item in args:
            if isinstance(item, float) == False:
                raise TypeError("argument must be float type")
            self._storage += (item,)

    def __str__(self):
        temp = []
        for item in self._storage:
            item = format(float(item), ".2f")
            temp.append(item)

        return f"{tuple(temp)}"

    def __repr__(self):
        temp = []
        for item in self._storage:
            item = format(float(item), ".2f")
            temp.append(item)
        return f"{tuple(temp)}"

    def __hash__(self):
        return hash(self._storage)

    def distanceFrom(self, element):
        index = 0
        if isinstance(element, Datum) == False:
            raise TypeError('Argument pass must be type Datum')
        if len(element._storage) < len(self._storage):
            index = len(self._storage) - len(element._storage)
            for i in range(0,index):
                element._storage += (0.0,)
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self._storage,element._storage)]))
        if index > 0:
            element._storage = element._storage[:-index]
        return distance

    def clone(self):
        newInstance = copy.deepcopy(self)
        return newInstance

    def __contains__(self, someFloat):
        if isinstance(someFloat, float) == False:
            raise TypeError('Argument pass must be type float')
        return someFloat in self._storage

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        return iter(self._storage)

    def __neg__(self):
        temp = []
        for item in self._storage:
            item = item * -1
            temp.append(item)
        temp = tuple(temp)
        self._storage = temp
        return self.clone()

    def __getitem__(self, index):
        return self._storage[index]

    def __isub__(self, other):
        if isinstance(other,Datum) == False:
            raise TypeError("Argument must be an instance of Datum")
        return self.clone()

    def __add__(self, other):
        temp = []
        if isinstance(other,Datum):
            if len(self._storage) < len(other._storage):
                index = len(other._storage) - len(self._storage)
                for i in range(0,index):
                    self._storage += (0.0,)
            elif len(self._storage) > len(other._storage):
                index = len(self._storage) - len(other._storage)
                for i in range(0, index):
                    other._storage += (0.0,)
            temp = [a + b for a, b in zip(self._storage,other._storage)]
            self._storage = tuple(temp)

        elif isinstance(other,float):
            for item in self._storage:
                item += other
                temp.append(item)
            self._storage = tuple(temp)

        else:
            raise TypeError("Argument must be an instance of Datum or float")
        return self.clone()

    def __sub__(self, other):
        temp = []
        if isinstance(other,Datum):
            if len(self._storage) < len(other._storage):
                index = len(other._storage) - len(self._storage)
                for i in range(0,index):
                    self._storage += (0.0,)
            elif len(self._storage) > len(other._storage):
                index = len(self._storage) - len(other._storage)
                for i in range(0, index):
                    other._storage += (0.0,)
            temp = [a - b for a, b in zip(self._storage,other._storage)]
            self._storage = tuple(temp)

        elif isinstance(other,float):
            for item in self._storage:
                item -= other
                temp.append(item)
            self._storage = tuple(temp)

        return self.clone()

    def __mul__(self, other):
        temp = []
        if isinstance(other,float) == False:
            raise TypeError("Argument must be type float")
        for item in self._storage:
            item *= other
            temp.append(item)
        self._storage = tuple(temp)
        return self.clone()

    def __truediv__(self, other):
        temp = []
        if isinstance(other,float) == False:
            raise TypeError("Argument must be type float")
        for item in self._storage:
            item /= other
            temp.append(item)
        self._storage = tuple(temp)

        return self.clone()

    def _createOrigin(self,other):
        temp = []
        for i in range(0, len(other._storage)):
            temp.append(1.0)
        temp = tuple(temp)
        return temp

    def __eq__(self, other):
        if isinstance(other,Datum) == False:
            raise TypeError("Argument must be type Datum")
        temp1 = self._createOrigin(self)
        distance1 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self._storage, temp1)]))
        temp2 = self._createOrigin(other)
        distance2 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(other._storage, temp2)]))
        return distance1 == distance2

    def __lt__(self, other):
        if isinstance(other,Datum) == False:
            raise TypeError("Argument must be type Datum")
        temp1 = self._createOrigin(self)
        distance1 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self._storage, temp1)]))
        temp2 = self._createOrigin(other)
        distance2 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(other._storage, temp2)]))
        return distance1 < distance2

    def __gt__(self, other):
        if isinstance(other,Datum) == False:
            raise TypeError("Argument must be type Datum")
        temp1 = self._createOrigin(self)
        distance1 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self._storage, temp1)]))
        temp2 = self._createOrigin(other)
        distance2 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(other._storage, temp2)]))
        return distance1 > distance2

    def __le__(self, other):
        if isinstance(other,Datum) == False:
            raise TypeError("Argument must be type Datum")
        temp1 = self._createOrigin(self)
        distance1 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self._storage, temp1)]))
        temp2 = self._createOrigin(other)
        distance2 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(other._storage, temp2)]))
        return distance1 <= distance2

    def __ge__(self, other):
        if isinstance(other,Datum) ==  False:
            raise TypeError("Argument must be type Datum")
        temp1 = self._createOrigin(self)
        distance1 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self._storage, temp1)]))
        temp2 = self._createOrigin(other)
        distance2 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(other._storage, temp2)]))
        return distance1 >= distance2

    def __ne__(self, other):
        if isinstance(other,Datum) == False:
            raise TypeError("Argument must be type Datum")
        temp1 = self._createOrigin(self)
        distance1 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self._storage, temp1)]))
        temp2 = self._createOrigin(other)
        distance2 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(other._storage, temp2)]))
        return distance1 != distance2

class Data:
    pass

class DataClass(Enum):
    Class1 = 1
    Class2 = 2

class DataClassifier:
    pass



# -----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    test = Datum(3.14, -900.7511, 33.9)
    print(test)
    test1 = Datum(1.0,2.0)
    print(test1)
    test2 = Datum(-1.54,7.10,9.00,15.33)
    print(test2)
    #print(test2.distanceFrom(test1))
    #print(33.1 in test)
    test3 = test1 - test2
    print(test3)
    print(test != test2)
    print(test3 * 3.9)