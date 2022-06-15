import numpy as np
import math

from scipy.linalg import sqrtm
def experimental(T,D,A,R,L,H,V):
    Y = np.array([[1,0]])
    I = np.array([[1,0],[0,1]])
    X = np.array([[1],[0]])
    print(Y)
    print(I)
    print(X)
    return np.matmul(X,np.matmul(I,Y))
   

print(experimental(5.6, .83, 4.6, .73, 4.8, 2.9, 2.4))
