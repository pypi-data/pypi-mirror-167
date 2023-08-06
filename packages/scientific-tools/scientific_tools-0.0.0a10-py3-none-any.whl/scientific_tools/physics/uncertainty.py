#changer le nom
"""Calculate standard uncertainty (standart uncertainty mainly)"""

import numpy as np

def standard_uncertainty(u_x, u_y, dz_dx, dz_dy) :
    """Calculate the standard uncertainty of z with the general formule."""
    return np.sqrt((u_x*dz_dx)**2+(u_y*dz_dy)**2)

def standard_uncertainty_addition(u_x, u_y, a=1, b=1) :
    """Calculate the standard uncertainty of z = ax + by (a & b const).
    
    a and b are constants define with no uncertainty
    """
    return np.sqrt((a**2)*(u_x**2)+(b**2)*(u_y)**2)

def relative_uncertainty_multiplication(ur_x, ur_y, a=1, b=1, c=1) :
    """Calculate the relative uncertainty of z= c*x^a*y^b (a, b, c const)
    
    a, b and c are constants define with no uncertainty
    c have no influance on the result
    ur(x) = u(x)/x. Idem for y.
    """
    return np.sqrt((a*ur_x)**2+(b*ur_y)**2)

def standard_uncertainty_multiplication(x, u_x, y, u_y, a=1, b=1, c=1) :
    """Calculate the standard uncertainty of z= c*x^a*y^b (a, b, c const)
    
    a, b and c are constants difine with no uncertainty
    """
    z = c*(x**a)*(y**b)
    return relative_uncertainty_multiplication(u_x/x, u_y/y, a, b, c)*abs(z)