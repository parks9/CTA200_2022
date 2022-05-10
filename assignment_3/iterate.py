import numpy as np


#%%
def iterate(x,y,N):
    """Iterates the complex number c = x + iy, through the equation
    z_{i+1} = z_{i}^2 + c, N times. Starting with z_{0} = 0


    
    For a given point on the compolex plane, c = x + iy, it is iterated through
    the equation z_{i+1} = z_{i}**2 + c, N times. The initial value is
    z_{0} = 0. A point is considered to diverge if it's square modulus is
    greater than 8 (outisde of the grid set by {-2, 2} X {-2, 2}). If a point
    does not diverge, its characteristic iteration number is set to zero.
    Otherwise, the iteration number at which it diverges is stored as num.


    Arguments
    ----------

    x : float
        Real part of the complex number c = x + iy.

    y : float
        Imaginary part of the complex number c = x + iy.

    N : int
        Number of iterations.

    
    Returns
    ----------

    z_list : array_like (complex)
        Array of all the N iterated values of z_{i}.

    z_mod : array_like (float)
        Array of the modulus squared (|z|^2) of the complex numbers
        stored in z_lst

    num : int
        Integer set to zero for points in the complex plane that do not
        diverge. Otherwise, will equal the iteration number at which the
        initial point (c = x +iy) diverges.

    """
    real = x
    imaj = y

    z = real + imaj*1j


    z_lst = np.zeros(N+1, dtype=complex)
    z_mod = np.zeros(N+1)

    z_lst[0], z_mod[0] = 0, 0

    for i in range(N):
        z_lst[i+1] = z_lst[i]**2 + z  

        z_mod[i+1] = (z_lst[i].real)**2 + (z_lst[i].imag)**2

    num = 0

    if len(np.where(z_mod > 8)[0]) > 0:
        num = np.where(z_mod > 8)[0][0]

    return z_lst, z_mod, num
