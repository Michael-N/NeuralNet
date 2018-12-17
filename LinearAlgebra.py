#./bin/python
'''
Code by: Michael S. Naguib
Date   : 12/16/18
License: MIT open source
@University of Tulsa
Description: a general purpose linear algebra library

## Documentation

### Class ```LinearAlgebra```
#### Properties
#### Methods

### Class ```Vector```
#### Properties
- ```values```: the array that stores the values for the vector... (should never be modified directly...)
#### Methods
- ```dot(otherVector)```: returns the dot product of the caller instance with the otherVector
- ```multiply(otherVector)```: returns the element wise multiplication of the caller instance with the otherVector as a new vector instance
- ```__mul__(otherVector)```: syntatic sugar using  * operand for calling mult(otherVector)  mult and __mul__ are the same logic
- ```length()```: returns the length of the vector
- ```__len__```: syntatic sugar using len(vectorInstance) for calling length()  length and __len__ are the same logic
- ```add(otherVector)```: returns a new vector instance that is the sum of the instance calling sum add and otherVector
- ```__add__```: syntatic sugar using + for calling add(otherVector)  add and __add__ are the same logic
- ```subtract(otherVector)```: returns a new vector instance that is the difference of the instance calling subtract and otherVector
- ```__sub__```: syntatic sugar using - for calling subtract(otherVector)  subtract and __sub__ are the same logic
- ```normalize```: returns (as a new instance) the result of normalizing the current vector 
'''
#imports
import copy
import math

class Vector:
    #TODO: check that #items match else error for every method etc... maybe add property so valList not recalculated...
    def __init__(self,valList):
        self.values = copy.deepcopy(valList)
    #Dot product on two same number of item vectors: returns the dot product  value
    def dot(self,otherVector):
        
        sum=0
        for i in range(0,len(self.values)):
            sum = sum + self.values[i]*otherVector.values[i]
        return sum
    #Multiplication of two vectors element wise
    def multiply(self,otherVector):
        newValList=[]
        for i in range(0,len(self.values)):
            newValList.append(self.values[i]*otherVector.values[i])
        return Vector(newValList)
    def __mul__(self,otherVector):
        return self.mult(otherVector)
    #Length of a vector:
    def length(self):
        return math.sqrt(self.dot(self))
    def __len__(self):
        return self.length()
    #Add two vectors together and get a new vector instance
    def add(self,otherVector):
        newValList=[]
        for i in range(0,len(self.values)):
            newValList.append(self.values[i] + otherVector.values[i])
        return Vector(newValList)
    def __add__(self,otherVector):
        return self.add(otherVector)
    #Subtract two vectors together and get a new vector instance
    def subtract(self,otherVector):
        newValList=[]
        for i in range(0,len(self.values)):
            newValList.append(self.values[i] - otherVector.values[i])
        return Vector(newValList)
    def __sub__(self,otherVector):
        return self.add(otherVector)
    #Normalize: returns a new instance representing the normalized current vector... 
    def normalize(self):
        #dot product of a vector with a vector of all 1s is the sum of that vector.... UPDATE: more efficient ways exist
        #sum = self.dot([1]*len(self.values)) 
        sum=0
        for num in self.values:
            sum = sum + num
        newValList = []
        for num in self.values:
            newValList.append(num/sum)
        return Vector(newValList)