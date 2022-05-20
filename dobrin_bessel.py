import numpy as np 
import scipy as sp
from scipy import special as spec # for bessel functions
from scipy.integrate import quad
import math 
from matplotlib import pyplot as plt 
pi = math.pi

# params 
dx = 0.s
dy = 0.
r = 1 # sigma x sigma y ratios , round beams = 1
xi = 0.0048 # beam-beam parameter 
qmax = 35


def BESS2D(a,b,n): 
    temp = []
    for i in np.arange(-qmax, qmax):
        temp.append(np.exp(-(a+b))*spec.iv(n-2*i,a)*spec.iv(i,b))
    return np.sum(temp)


def g(x,r): 
    ans = np.sqrt(1+(r^2-1)*x)
    return ans

def DXC00(x): 
    axbar = ax*r
    aybar = ay/g(x,r)
    dxbar = dx
    dybar = dy*r/g(x,r)
    U1x = axbar*dxbar
    U2x = -0.25*axbar**2
    U1y = aybar*dybar
    U2y = -0.25*aybar**2
    
    return -r/g(x,r)*np.exp(-(x/2)*((axbar-dxbar)**2+(aybar-dybar)**2))*BESS2D(U1y*x,U2y*x,0)*(-axbar*0.5*(BESS2D(U1x*x,U2x*x,0)+BESS2D(U1x*x,U2x*x,2))+dxbar*BESS2D(U1x*x,U2x*x,1))
      
    
def DYC00(x): 
    axbar = ax*r
    aybar = ay/g(x,r)
    dxbar = dx
    dybar = dy*r/g(x,r)
    U1x = axbar*dxbar
    U2x = -0.25*axbar**2
    U1y = aybar*dybar
    U2y = -0.25*aybar**2
    
    return -r/g(x,r)*np.exp(-(x/2)*((axbar-dxbar)**2+(aybar-dybar)**2))*BESS2D(U1x*x,U2x*x,0)*(-aybar*0.5*(BESS2D(U1y*x,U2y*x,0)+BESS2D(U1y*x,U2y*x,2))+dybar*BESS2D(U1y*x,U2y*x,1))
      
def dqxy(ax,ay,DXC00,DYC00,dx,dy,r,xi): 
    axi = -2*xi*DXC00/ax
    ayi = -2*xi*DYC00/ay
    dqxyi=[axi,ayi]
    return dqxyi

def points(r,n):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

def make_amp_distribution(min_amp,max_amp):
    dist=[]
    for k in np.arange(min_amp,max_amp):
        a = np.array(points(k,n=25)) # make this a loop 
        for i in range(len(a)): 
            if a[i][0] >0.01 and a[i][1] > 0.01:
                dist.append(a[i])
    return dist 

# make the initial distribution in amplitudes 

particles = make_amp_distribution(1,6)

tunesx =[]
tunesy = []

for i in range(len(particles)):
    ax = particles[i][0]
    ay = particles[i][1]
    dytemp = 0 
    dxtemp = 0 
    xi = 0.00488
    c = quad(DXC00,0,1)
    d = quad(DYC00,0,1)
    dq=dqxy(ax,ay,c[0],d[0],dx,dy,r,xi)
    tunesx.append(dq[0])
    tunesy.append(dq[1])


# scatter plot

normtx = (2*np.array(tunesx))/(2*xi) # for 2 HO
normty = (2*np.array(tunesy))/(2*xi)
points=15
plt.scatter(normtx,normty, alpha=0.5, s=points)  
plt.xlabel('$Q_{x}/2\zeta$')
plt.ylabel('$Q_{y}/2\zeta$')
plt.title('Title')
plt.savefig('./your_detuning.png')
