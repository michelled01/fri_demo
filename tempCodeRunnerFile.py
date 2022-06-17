import cmath
# import numpy as np
# import math
# import scipy
# from scipy.linalg import sqrtm

# ### fidelity ###

# def HWP(theta):
#     tl = math.cos(2*theta)
#     tr = math.sin(2*theta)
#     bl = math.sin(2*theta)
#     br = (-1)*math.cos(2*theta)
#     return np.array([[tl, tr], [bl, br]])

# def QWP(phi):
#     tl = pow(math.cos(phi),2)+1j*pow(math.sin(phi),2)
#     tr = (1-1j)*math.sin(phi)*math.cos(phi)
#     bl = (1-1j)*math.sin(phi)*math.cos(phi)
#     br = pow(math.sin(phi),2)+1j*pow(math.cos(phi),2)
#     return np.array([[tl, tr], [bl, br]])

# #calculates the final theoretical vector |v>
# def pure_state(theta, phi):
#     #init
#     hwp = HWP(theta)
#     qwp = QWP(phi)
#     H = np.array([[1.0],[0.0]])
#     #calc
#     return np.matmul(qwp, np.matmul(hwp,H))
    
# def outer_product(PS):
#     PS_t = np.conj(np.transpose(PS))
#     return np.matmul(PS,PS_t)

# #calculate expectation values and computes density matrix
# def experimental(T,D,A,R,L,H,V):
#     #calc expectation vals
#     expX = (D-A)/T
#     expY = (R-L)/T
#     expZ = (H-V)/T

#     #init matricies
#     I = np.array([[1.0,0.0],[0.0,1.0]])
#     X = np.array([[0.0,1.0],[1.0,0.0]])
#     Y = np.array([[0.0,-1j],[1j,0.0]])
#     Z = np.array([[1.0,0.0],[0.0,-1.0]])
    
#     #density matrix calc
#     return 0.5*(I + expX*X + expY*Y + expZ*Z)

# def fidelity(PS, exp_DS):
#     bra = np.conj(np.transpose(PS))
#     mid = exp_DS
#     ket = PS
#     return np.matmul(bra,np.matmul(mid,ket))

# def error(f):
#     return 1-f

# ### trace distance ###
# def traceDist(theo_DS, exp_DS):
#     diff = theo_DS - exp_DS
#     diff_t = np.conj(np.transpose(diff))
#     square = np.matmul(diff,diff_t)
#     sqrt_matrix = sqrtm(square)
#     mat = sqrt_matrix
#     sum = 0
#     for i in range(len(mat)):
#        sum += mat[i][i]
#     return sum/2
