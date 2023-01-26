 
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
no_of_colors=15
zenith = [45,50,55,60,65,70,75,77.5,80,82.5,85,86,87,87.5,88]
colors = [plt.cm.nipy_spectral(i) for i in np.linspace(0, 1, no_of_colors+1)]
Gramms=np.reshape(Gramms,(len(zenith),len(grammage),2))
plt.figure(dpi=100)
for i in range(len(zenith)):
    plt.plot(Gramms[i,:,0],Gramms[i,:,1],color=colors[i],label='%.1f deg'%zenith[i])
#plt.legend( prop={'size': 15.5},title='Zenith[$^\circ$]',title_fontsize=17,bbox_to_anchor=(1.01,1.08), loc='upper left') 
plt.xlabel('Shower Depth [g/cm$^2$]')
plt.ylabel('Radius of cherrenkov ring [m]')
#plt.gca().invert_xaxis()
plt.xlim(520,1200)
plt.ylim(0,2700)
plt.grid()
plt.show()