import cmath
# import numpy

a = 4+3j
b = 5+2j
print(a*b)

# calculate fidelity and trace distance

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
        # for square rooting, https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.sqrtm.html
