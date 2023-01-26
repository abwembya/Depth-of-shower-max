import numpy as np
import mplhep as hep
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
hep.style.use("ATLAS")
import os 
grammage = np.linspace(550,1200,10)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Gramms2=np.load('Gramms2.npy')
no_of_colors=15
zenith = [45,50,55,60,65,70,75,77.5,80,82.5,85,86,87,87.5,88]
colors = [plt.cm.nipy_spectral(i) for i in np.linspace(0, 1, no_of_colors+1)]
Gramms2=np.reshape(Gramms2,(len(zenith),len(grammage),2))
plt.figure(dpi=100)
for i in range(len(zenith)):
    plt.plot(Gramms2[i,:,0],np.gradient(Gramms2[i,:,1],Gramms2[i,:,0]),color=colors[i],label='%.1f deg'%zenith[i])
plt.legend( prop={'size': 14},title='Zenith',title_fontsize=15, loc='best',bbox_to_anchor=(1.01, 1),borderaxespad=0.)
plt.xlabel('Shower Depth [g/cm$^2$]')
plt.ylabel('Derivative [m/g/cm$^2$]')
#plt.gca().invert_xaxis()
#plt.yscale('log')
plt.xlim(min(grammage),max(grammage))
plt.xlim(540,1200)
plt.ylim(-0.25,0.5)
plt.grid()
plt.show()