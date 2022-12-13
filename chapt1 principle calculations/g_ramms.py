 
import numpy as np
import mplhep as hep
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
hep.style.use("ATLAS")
import os 
grammage = np.linspace(550,1200,10)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Gramms=np.load('Gramms.npy',allow_pickle=True)
no_of_colors=17
zenith = np.linspace(45,85,no_of_colors)
colors = [plt.cm.nipy_spectral(i) for i in np.linspace(0, 1, no_of_colors+1)]
Gramms=np.reshape(Gramms,(len(zenith),len(grammage),2))
plt.figure(dpi=100)
for i in range(len(zenith)):
    plt.plot(Gramms[i,:,0],Gramms[i,:,1],color=colors[i],label='%.1f deg'%zenith[i])
plt.legend( prop={'size': 12},title='Zenith',title_fontsize=13, loc='best',bbox_to_anchor=(1.05, 1),borderaxespad=0.)
plt.xlabel('Grammage [g/cm$^2$]')
plt.ylabel('Distance to core [m]')
plt.xlim(570,1200)
plt.grid()
plt.show()