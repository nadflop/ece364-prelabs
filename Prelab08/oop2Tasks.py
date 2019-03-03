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
from collections import UserList
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
            self._storage = temp
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

class Data(UserList):

    def __init__(self, initial = None):
        if initial is not None:
            for item in initial:
                if isinstance(item,Datum) == False:
                    raise TypeError("Argument must be type Datum")
            super().__init__(initial)

        if initial == None:
            super().__init__([])

    def computeBounds(self):
        maxLen = 0
        minCord = []
        maxCord = []
        for item in self.data:
            maxLen = max(maxLen, len(item),key=int)

        for item in self.data:
            if len(item) < maxLen:
                for i in range(0, 3 - len(item)):
                    item._storage = item._storage + (0.0,)

        for i in range(0, maxLen):
            minCord.append(self.data[0][i])
            maxCord.append(self.data[0][i])

        for item in self.data:
            for i in range(0, maxLen):
                minCord[i] = min(minCord[i], item[i])
                maxCord[i] = max(maxCord[i],item[i])

        minDatum = Datum(*minCord)
        maxDatum = Datum(*maxCord)

        return  (minDatum,maxDatum)

    def computeMean(self):
        maxLen = 0
        minCord = []
        for item in self.data:
            maxLen = max(maxLen, len(item),key=int)

        for item in self.data:
            if len(item) < maxLen:
                for i in range(0, 3 - len(item)):
                    item._storage = item._storage + (0.0,)

        for i in range(0, maxLen):
            minCord.append(0.0)

        for item in self.data:
            for i in range(0, maxLen):
                minCord[i] += item[i]

        for i in range(0,maxLen):
            minCord[i] = minCord[i]/maxLen
        return Datum(*minCord)

    def append(self, item):
        if isinstance(item,Datum) == False:
            raise TypeError('argument must be type Datum')
        return super().append(item)

    def count(self, item):
        if isinstance(item,Datum) == False:
            raise TypeError('argument must be type Datum')
        return super().count(item)

    def index(self, item, *args):
        if isinstance(item,Datum) == False:
            raise TypeError('argument must be type Datum')
        return super().index(item, *args)

    def insert(self, i, item):
        if isinstance(item,Datum) == False:
            raise TypeError('argument must be type Datum')
        return super().insert(i, item)

    def remove(self, item):
        if isinstance(item,Datum) == False:
            raise TypeError('argument must be type Datum')
        return super().remove(item)

    def __setitem__(self, key, value):
        self.data[key] = value

    def extend(self, other):
        if isinstance(other,Datum) == False:
            raise TypeError('argument must be type Datum')
        super().extend(other)


class DataClass(Enum):
    Class1 = 1
    Class2 = 2

class DataClassifier:
    _class1 = None
    _class2 = None

    def __init__(self, group1, group2):
        if isinstance(group1,Data) == False:
            raise TypeError("Group1 must be an instance of Data")
        if isinstance(group2,Data) == False:
            raise TypeError("Group2 must be an instance of Data")
        if len(group1) == 0:
            raise ValueError("Group1 must not be empty")
        if len(group2) == 0:
            raise ValueError("Group2 must not be empty")

        self._class1 = group1
        self._class2 = group2

    def classify(self, otherDatum):
        mean1 = self._class1.computeMean()
        mean2 = self._class2.computeMean()
        if len(otherDatum) < len(mean1):
            for i in range(0, len(mean1) - len(otherDatum)):
                otherDatum._storage += (0.0,)
        elif len(otherDatum) > len(mean1):
            temp = tuple(mean1)
            for i in range(0, len(otherDatum) - len(mean1)):
                temp += (0.0,)
            mean1 = temp
        distance1 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(mean1, otherDatum)]))

        if len(otherDatum) < len(mean2):
            for i in range(0, len(mean2) - len(otherDatum)):
                otherDatum._storage += (0.0,)
        elif len(otherDatum) > len(mean2):
            temp = tuple(mean2)
            for i in range(0, len(otherDatum) - len(mean2)):
                temp += (0.0,)
            mean2 = temp
        distance2 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(mean2, otherDatum)]))

        if distance1 < distance2:
            return DataClass.Class1
        elif distance1 > distance2:
            return DataClass.Class2
        else:
            return DataClass.Class1

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ...