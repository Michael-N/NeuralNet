#./bin/python
'''
Code by: Michael S. Naguib
Date   : 12/17/18
License: MIT open source
@University of Tulsa
Description: testing script for the library
'''
#import library
LinearAlgebra = __import__("LinearAlgebra")
V = LinearAlgebra.Vector
M = LinearAlgebra.Matrix

#Begin
if __name__ == "__main__":
    a = M([[1,2,3],[4,5,6],[7,8,9]])
    b = M([[9,8,7],[6,5,4],[3,2,1]])
    r = a.multiply(b)
    print (str(r))