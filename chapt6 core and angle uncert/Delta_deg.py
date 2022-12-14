import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep
import os
plt.style.use(hep.style.ATLAS)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
delta_theta=np.loadtxt('delta_theta.npy')

zenith = np.linspace(45,85,10)
plt.plot(zenith,delta_theta[0],color='b',label='10')
plt.plot(zenith,delta_theta[1],color='g',label='30')
plt.plot(zenith,delta_theta[2],color='r',label='50')
plt.plot(zenith,delta_theta[3],color='y',label='100 ')
plt.legend( prop={'size': 13},title='$\sigma_{x_{max}}~~~[g/cm^2]$' ,title_fontsize=13)
plt.xlabel(r'Zenith  [deg]')
plt.ylabel(r'$\sigma_\theta$ [deg]')
plt.yscale('log')
plt.grid()
plt.xlim(45,85)
plt.savefig('Delta_theta.png',dpi=300)
plt.show()