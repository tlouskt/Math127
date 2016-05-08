import numpy as np 
import matplotlib as plt
from scipy.interpolate import RegularGridInterpolator

"""
Goal project_fst_mo

1.  Compute 3D DFT of molecule mol, producing F(mol) another 3D Array
2.  Restrict F(mol) to the image plane P_f thus producing a 2D Array
3.  Compute IFFT of the restriction above

Note that for interpolation you should use grid interpolator object (
    i.e. returns obsject that will sample the function mol at any point)
    Documentation should help
"""

def project_fst(mol, R):
    """
    Creates an "image" given NxNxN matrix representation of mol and rotation 
    matrix R
    Args:
         mol: An NxNxN array that serves as an approximation for a function
              from R^3 --> R
         R:   rotation matrix [a,b,c] (a,b,c correspond to row vectors)

    Returns:
        NxN 2darray "Image"  
    """
    mol_hat = np.fft.fftn(mol)
    # Fix the coordinate system mol_hat should really be centered
    # at the origin
    mol_hat = np.fft.fftshift(mol_hat)
    # For now assume that we want image to be size of mol
    # (Could actually choose anything here kind of arbitrary)
    N = mol.shape[0]
    N_range = np.array(range(N))
    inter = RegularGridInterpolator((N_range, N_range, N_range), mol_hat,method='linear', bounds_error=False, fill_value=0)

    trans = np.zeros((N, N, 3))
    for i in np.arange(N):
        for j in np.arange(N):
            # Now we need to change our i,j coordinates to x,y coordnitates
            # column changing corresponds to x chan ging and vice versa
            x = -(N-1)/2 + j
            y = (N-1)/2 - i
            # Now we must get our p_vector using span(a,b)
            p = R[:, 0]*x + R[:, 1]*y
            # Note that p vector is a vector from R^3
            # Now we must change p from x,y,z to i_,j_,k_
            # Because we will use these points to sample from mol_hat
            i_ = float(N-1)/2 - p[1]
            j_ = p[0] + float(N-1)/2
            k_ = float(N-1)/2 - p[2]  # note this direction is arbitrary k is going
            # from top down with highest point  corresponding to 0
            trans[i, j] = i_, j_, k_
    I = inter(trans)

    comp = np.fft.ifft2(I)
    ans = np.zeros((N, N))
    for i in np.arange(N):
        for j in np.arange(N):
            ans[i][j] = np.linalg.norm(comp[i][j])
    return ans



