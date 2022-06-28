# %%
import numpy as np
from matplotlib import pyplot as plt
from bb_tools import bassetti_erskine as be

# %%
sig_x = 1e-5
sig_y = sig_x*0.999999

x = 2*sig_x
y = 1*sig_y
N = 1.8e11
gamma = 7000
# %%
be.bassetti_erskine_kick(x, y, N, sig_x, sig_y, gamma)

# %%
x_samples = np.linspace(-5*sig_x,5*sig_x)

# Calculate the BE kick
BE_kick_imag = np.vectorize(lambda x: np.imag(be.bassetti_erskine_kick(x, y, N, sig_x, sig_y, gamma)))
plt.plot(x_samples, BE_kick_imag(x_samples))

# Calculate the round beam kick 
RB_kick = np.vectorize(lambda x: np.imag(be.round_gaussian_kick(x, y, N, sig_x, gamma))) # shouldnt be imaginary? 
plt.plot(x_samples, RB_kick(x_samples), 'or')

# %%
# Calculate BE kick 
BE_kick_real = np.vectorize(lambda x: np.real(be.bassetti_erskine_kick(x, y, N, sig_x, sig_y, gamma)))
plt.plot(x_samples, BE_kick_real(my_x))


# Calculate the RB kick
RB_kick = np.vectorize(lambda x: np.real(be.round_gaussian_kick(x, y, N, sig_x, gamma)))
plt.plot(x_samples, RB_kick(x_samples), 'or') 

# %%
