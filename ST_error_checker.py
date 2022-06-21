import cmath
import numpy as np
import math
import scipy
from scipy.linalg import sqrtm

''' process for calculating fidelity and trace distance:
    # fidelity 
        # theoretical
            # get theta and phi 
            # multiply QWP(phi)*HWP(theta)*|H> = pure state
            # do the outer product = theo density matrix
        # experimental
            # get P_i (Total T)
            # get counts (D,A,R,L,H,V)
            # calculate expectations (<X> = (D-A)/T, <Y> = (R-L)/T, <Z> = (H-V)/T)
            # calculate the exp. density matrix
        # comparison
            # F = <PS| exp.DS |PS>
            # ε = 1-F
        
    # trace distance
        # TD = 0.5*Tr[sqrt((ρ-φ)ᵗ(ρ-φ))] 
        # for subtraction, use the DS's we got from fidelity
        # for square rooting, https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.sqrtm.html '''

### fidelity ###

def HWP(theta):
    tl = math.cos(2*theta)
    tr = math.sin(2*theta)
    bl = math.sin(2*theta)
    br = (-1)*math.cos(2*theta)
    return np.array([[tl, tr], [bl, br]])

def QWP(phi):
    tl = pow(math.cos(phi),2)+1j*pow(math.sin(phi),2)
    tr = (1-1j)*math.sin(phi)*math.cos(phi)
    bl = (1-1j)*math.sin(phi)*math.cos(phi)
    br = pow(math.sin(phi),2)+1j*pow(math.cos(phi),2)
    return np.array([[tl, tr], [bl, br]])

#calculates the final theoretical vector |v>
def pure_state(theta, phi):
    #init
    hwp = HWP(theta)
    qwp = QWP(phi)
    H = np.array([[1.0],[0.0]])
    #calc
    return np.matmul(qwp, np.matmul(hwp,H))
    
def outer_product(PS):
    PS_t = np.conj(np.transpose(PS))
    return np.matmul(PS,PS_t)

#calculate expectation values and computes density matrix
def experimental(T,D,A,R,L,H,V):
    #calc expectation vals
    expX = (D-A)/T
    expY = (R-L)/T
    expZ = (H-V)/T

    #init matricies
    I = np.array([[1.0,0.0],[0.0,1.0]])
    X = np.array([[0.0,1.0],[1.0,0.0]])
    Y = np.array([[0.0,-1j],[1j,0.0]])
    Z = np.array([[1.0,0.0],[0.0,-1.0]])
    
    #density matrix calc
    return 0.5*(I + expX*X + expY*Y + expZ*Z)

def altExperimental(T1,T2, T3,D,A,R,L,H,V):
    #calc expectation vals
    expX = (D-A)/T1
    expY = (R-L)/T2
    expZ = (H-V)/T3

    #init matricies
    I = np.array([[1.0,0.0],[0.0,1.0]])
    X = np.array([[0.0,1.0],[1.0,0.0]])
    Y = np.array([[0.0,-1j],[1j,0.0]])
    Z = np.array([[1.0,0.0],[0.0,-1.0]])
    
    #density matrix calc
    return 0.5*(I + expX*X + expY*Y + expZ*Z)

def fidelity(PS, exp_DS):
    bra = np.conj(np.transpose(PS))
    mid = exp_DS
    ket = PS
    return np.matmul(bra,np.matmul(mid,ket))

def error(f):
    return 1-f


### trace distance ###

def traceDist(theo_DS, exp_DS):
    diff = theo_DS - exp_DS
    diff_t = np.conj(np.transpose(diff))
    square = np.matmul(diff,diff_t)
    sqrt_matrix = sqrtm(square)
    mat = sqrt_matrix
    sum = 0
    for i in range(len(mat)):
       sum += mat[i][i]
    return sum/2

    
#Testing WebApp
def go(theta, phi,totalPower,Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts):
    theta = math.radians(theta)
    phi = math.radians(phi)
    PS = pure_state(theta,phi)
    exp_DS = experimental(totalPower,Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts)
    fid = fidelity(PS,exp_DS)[0][0]
    err = error(fidelity(PS,exp_DS)[0][0])
    trD = traceDist(experimental(totalPower,Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts), outer_product(PS))
    return [err,trD]

def convertPercentage(res):
    res[0] = res[0]*100
    res[1] = res[1]*100
    return res

def altGo(theta, phi,tp1,tp2,tp3,Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts):
    theta = math.radians(theta)
    phi = math.radians(phi)
    PS = pure_state(theta,phi)
    exp_DS = altExperimental(tp1, tp2, tp3, Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts)
    fid = fidelity(PS,exp_DS)[0][0]
    err = error(fidelity(PS,exp_DS)[0][0])
    trD = traceDist(altExperimental(tp1, tp2, tp3,Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts), outer_product(PS))
    return [err,trD]

''' manual testing (outdated):
# testing fidelity (input in degrees)
print("enter preparation theta: ")
theta = float(input())
theta = math.radians(theta)
print("enter preparation phi: ")
phi = float(input())
phi = math.radians(phi)

print("enter total power: ")
totalPower = float(input())
print("enter recorded H count: ")
Hcounts = float(input()) 
print("enter recorded V count: ")
Vcounts = float(input()) 
print("enter recorded D count: ")
Dcounts = float(input()) 
print("enter recorded A count: ")
Acounts = float(input()) 
print("enter recorded R count: ")
Rcounts = float(input()) 
print("enter recorded L count: ")
Lcounts = float(input()) 

PS = pure_state(theta,phi)
#testing experimental
exp_DS = experimental(totalPower,Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts)
print("error: ", error(fidelity(PS,exp_DS)[0][0]))

#testing trace
print("trace distance: ",str(traceDist(experimental(totalPower,Dcounts,Acounts,Rcounts,Lcounts,Hcounts,Vcounts), outer_product(PS))))

'''