import itertools
import os
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

# Set the style
plt.style.use(hep.style.CMS)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sigmas=np.load('sigma_r.npy')
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
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
plt.savefig('sigma_r.png',dpi=300)


del_th_2=np.load('del_th_minus_25.npy',allow_pickle=True)
del_th_3=np.load('del_th_plus_25.npy',allow_pickle=True)

plt.figure(dpi=100)

zenith = np.linspace(40, 86, 25)

plt.plot(zenith, del_th_2[:25], color='red', label='data', alpha=0.7, linestyle='-')
plt.plot(zenith, del_th_2[25:50], color='green', alpha=0.7, linestyle='-')
plt.plot(zenith, del_th_2[50:75], color='blue', alpha=0.7, linestyle='-')
plt.plot(zenith, del_th_2[75:100], color='black', alpha=0.7, linestyle='-')

plt.plot(zenith, del_th_3[:25], color='red', label='data', alpha=0.7, linestyle=':')
plt.plot(zenith, del_th_3[25:50], color='green', alpha=0.7, linestyle=':')
plt.plot(zenith, del_th_3[50:75], color='blue', alpha=0.7, linestyle=':')
plt.plot(zenith, del_th_3[75:100], color='black', alpha=0.7, linestyle=':')

# Creating legends
lines = plt.gca().get_lines()
legend1 = plt.legend(lines[:4], ['10 g/cm$^2$', '30 g/cm$^2$', '50 g/cm$^2$', '100 g/cm$^2$'],
                     title=r'-$\Delta_{X_{750}}$', title_fontsize=17, loc='lower center',
                     labelspacing=0.01, frameon=True, facecolor='white', framealpha=0.5,
                     fancybox=True, edgecolor='black', borderpad=0.5)

legend2 = plt.legend(lines[4:8], ['-10 g/cm$^2$', '-30 g/cm$^2$', '-50 g/cm$^2$', '-100 g/cm$^2$'],
                     title='+$\Delta_{X_{750}}$', title_fontsize=17, loc='lower left',
                     labelspacing=0.01, frameon=True, facecolor='white', framealpha=0.5,
                     fancybox=True, edgecolor='black', borderpad=0.5)

plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)
plt.xlim(40, 86)
plt.grid(linestyle='--', linewidth=0.5)
plt.yscale('log')
plt.ylim( 0.001, 20)
plt.xlabel(r'$\theta$ [$^\circ$]', fontsize=20)
plt.ylabel(r'$\Delta _\theta$ [$^\circ$]', fontsize=20)
plt.show()
