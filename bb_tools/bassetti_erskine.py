# %%
from scipy import constants
import numpy as np 
import scipy
from scipy import constants
import scipy.special as ss 

q = constants.e
c = constants.c
m_p = constants.proton_mass
pi = np.pi
eps0 = constants.epsilon_0
r_p = q*q/(4*pi*eps0*c*c*m_p) # proton radius

def bassetti_erskine_kick(x, y, N, sig_x, sig_y, gamma, species='proton'):
    '''
    The kick delta x due to a thin element beam beam lens for Head On interactions 
    for proton beams. 
    '''
    
    if not (species == 'proton'):
        raise NotImplementedError
    #kick_BE.append(Force/(c**2*m_p*gamma))
    force = bassetti_erskine_force(x, y, N, sig_x,sig_y)
    kick = force/(c**2*m_p*gamma)
    return kick

def bassetti_erskine_force(x, y, N, sig_x,sig_y):
    '''
    The force due to a thin beam beam interaction for HO collisions for proton beams. 
    https://accelconf.web.cern.ch/hb2016/papers/mopr025.pdf
    '''
    z = complex(x,y)
    l = (N*q)/(2*eps0*np.sqrt(2*pi*(sig_x**2-sig_y**2)))
    m = ss.wofz(z/(np.sqrt(2*(sig_x**2-sig_y**2))))
    n = np.exp(-x**2/(2*sig_x**2)-y**2/(2*sig_y**2))
    o = ss.wofz((x*sig_y/sig_x+1j*y*sig_x/sig_y)/np.sqrt(2*(sig_x**2-sig_y**2)))
    force = l*(m-n*o)*q
    return force
    
def round_gaussian_force(x, y, N, sig):
    '''
    In the round beam approximation, sig_x=sig_y, the force due to a HO beam-beam interaction 
    for protons. 
    '''
    radius = np.sqrt(x**2+y**2)
    z = complex(y, x)
    r_p
    return (c**2*m_p)*(2*N*r_p)*(z/radius**2)*(1-np.exp(-radius**2/(2*sig**2)))

def round_gaussian_kick(x, y, N, sig, gamma, species='proton'):
    '''
    In the round beam approximation, the kick due to a beam beam HO interaction for protons. 
    https://cdsweb.cern.ch/record/1982430/files/431-459%20Herr.pdf
    '''
    if not (species == 'proton'):
        raise NotImplementedError
    force = round_gaussian_force(x, y, N, sig)
    kick = force/(c**2*m_p*gamma)
    return kick
