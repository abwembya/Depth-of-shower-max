
import numpy as np
from matplotlib import cbook
import matplotlib.colors
import matplotlib.pyplot as plt
import mplhep as hep
import os
hep.set_style("ATLAS")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#plots the integrated power in the pixels as a function of the sigma 

appndata = np.genfromtxt("cmaps",delimiter=",", dtype=float)
appndata=np.reshape(appndata,(6,3,10000))
jitter = [0,1,3,5,7,9]
fig, axes = plt.subplots(nrows=2, ncols=3, 
                        figsize=([12, 9]), constrained_layout=True,sharex=True,sharey=True)
i=0
for ax in axes.flat:
    im =  ax.hexbin(appndata[i][0],appndata[i][1],C=appndata[i][2],gridsize=45, vmin=0,vmax=1.5*10**11, cmap='inferno')
    #im = ax.scatter(appndata[i][0],appndata[i][1],c=appndata[i][2],s=5000,marker='s',vmin=0,vmax=2.5*10**11)
    ax.set_title('gauss(0,%d)'%jitter[i])
    i+=1
fig.colorbar(im, ax=axes.ravel().tolist(),label='amplitude')
fig.supxlabel('Distance [m]',fontsize=20)
fig.supylabel('Distance [m]',fontsize=20)
fig.suptitle('Integrated power in the pixels as a function of the sigma',fontsize=20)
plt.xlim(-2000,2000)
plt.ylim(-2000,2000)
plt.savefig('cmaps.png')
plt.show()
