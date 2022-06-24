import numpy as np 
import scipy
from scipy import constants
import scipy.special as ss 
from matplotlib import pyplot as plt 


q = scipy.constants.e
c = scipy.constants.c
m_p = scipy.constants.proton_mass
pi = np.pi
eps0 = scipy.constants.epsilon_0
N=1.8e11
gamma=6800/0.938
beta = np.sqrt(1-1/gamma**2)
r_p = q*q/(4*np.pi*eps0*c*c*m_p) # proton radius

# BESSETTI-ERSKINE


sig_x = np.sqrt(1.001e-10) # converting between sigma and epsilon x... 
sig_y = np.sqrt(1e-10)


x=np.linspace(sig_x*30,-sig_x*30,1000)
y = 0
z = [] # complex of x and y
for i in range(len(x)):
    z.append(complex(x[i],y))

kick_BE = []
Force_BE = []
for i in range(len(x)):
    l = (N*q)/(2*eps0*np.sqrt(2*pi*sig_x**2-sig_y**2))
    m = ss.wofz(z[i]/(np.sqrt(2*sig_x**2-sig_y**2)))
    n = np.exp(-x[i]**2/(2*sig_x**2)-y**2/(2*sig_y**2))
    o = ss.wofz((x[i]*sig_y/sig_x+1j*y*sig_x/sig_y)/np.sqrt(2*sig_x**2-sig_y**2))
    Force = l*(m-n*o)*q
    Force_BE.append(Force)
                    
    kick_BE.append(Force/(c**2*m_p*gamma)) # from the field to the kick 

    
    
# ROUND BEAMS 

sigma = np.sqrt(1.000e-10)

kick_RB = []
radius=[]
for i in range(len(x)):
    radius= (np.sqrt(x[i]**2+y**2))  # radius of x,y 
    kick_RB.append((-2*N*r_p/gamma)*(x[i]/radius**2)*(1-np.exp(-radius**2/(2*sigma**2)))) # why negative? 
    
# plot 
    
plt.plot(x/sig_x,np.imag(kick_BE), label='Bassetti Erskine $\sigma_x$=2*$\sigma_y$')
plt.plot(x/sigma,kick_RB, label='RB $\sigma_x$=$\sigma_y$')
plt.xlabel('$\sigma_x$')
plt.ylabel('$\Delta x\'$')
plt.title('Kick in x, y=0')
plt.legend()
