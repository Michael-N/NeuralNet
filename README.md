# NeuralNet
- Code By Michael S. Naguib
- License: MIT open source
- Date: 12/16/18
- @University of Tulsa
- Description: Code for implementing a small neural network; (also contains a lib for LinearAlgebra operations on matricies and vectors)
> UPDATE! as of lately the code for the neural net has been kept on the pc and not been pushed; this project is now going to evolve... 
A private repo will host the neural net code that I am working on; I plan to make it public but would like more freedom to expirament; if you would like to view msg me and I will see about making it public. 

## About:
- An expirament to code a neural network using matrix operations
- The file ```LinearAlgebra.py``` contains classes for matrix,vector,and general linear algebra operations and structures

## TODO:
- Work on ```Matrix``` and ```LinearAlgebra``` classes
- Create the method ```changeBasis``` and ```cross```for the ```Vector``` class (may need a few matrix operations...)

## Documentation

### Class ```LinearAlgebra```
#### Properties
#### Methods

### Class ```Matrix```
#### Properties
- ```values```: the array that stores the  nested arrays and values for the Matrix... (should never be modified directly...)
#### Methods
- ```multiply(otherVector)```: returns the matrix multiplication of the two matricies as a new matrix instance
- ```toString```: returns a string representation of the object
- ```__str__```: syntatic sugar for str(thisMatrixInstance)

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
