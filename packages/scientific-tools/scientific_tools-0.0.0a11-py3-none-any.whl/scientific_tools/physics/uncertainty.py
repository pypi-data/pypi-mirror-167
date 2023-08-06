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

def z_score_ref(x, x_ref, u_x):
    """Calculate the z-score between a measured value and a reference value.
    
    x is the measured value, x_ref the reference value and u_x the uncertainty
    """
    return abs((x-x_ref)/u_x)

def z_score(x1, u_x1, x2, u_x2) :
    """Calculate the z-score between two measured values
    
    x1 is the first value, x2 the second
    u_x1 is the uncertainty for x1, u_x2 for x2
    """
    return abs(x1-x2)/np.sqrt(u_x1**2 + u_x2**2)