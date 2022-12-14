import itertools
import os
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

# Set the style
plt.style.use(hep.style.CMS)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sigmas=np.load('sigmas.npy')
s4=int(sigmas.size/4)
sigmas10=sigmas[:s4]
sigmas30=sigmas[s4:s4*2]
sigmas50=sigmas[s4*2:s4*3]
sigmas100=sigmas[s4*3:s4*4]
plt.plot(np.rad2deg(sigmas10[::2]),abs(sigmas10[::-2][::-1]),color='b',label='%.1f '%10)
plt.plot(np.rad2deg(sigmas30[::2]),abs(sigmas30[::-2][::-1]),color='r',label='%.1f '%30)
plt.plot(np.rad2deg(sigmas50[::2]),abs(sigmas50[::-2][::-1]),color='g',label='%.1f '%50)
plt.plot(np.rad2deg(sigmas100[::2]),abs(sigmas100[::-2][::-1]),color='y',label='%.1f '%100)
plt.xlabel(r'Zenith [deg]')
plt.ylabel(r'$\sigma_r$ [m]')
plt.xlim(37,87)
plt.legend( prop={'size': 13},title='$\sigma_{x_{max}}~[g/cm^2]$',title_fontsize=15.5, loc='best')
plt.grid()
plt.show()
plt.savefig('sigma_r.png',dpi=300)