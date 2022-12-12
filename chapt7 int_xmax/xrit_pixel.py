
import numpy as np
from matplotlib import cbook
import matplotlib.colors
import matplotlib.pyplot as plt
import mplhep as hep
from mpl_toolkits.axes_grid1 import ImageGrid

#plots the integrated power in the pixels as a function of the sigma 

appndata = np.genfromtxt("cmaps",delimiter=",", dtype=float)
appndata=np.reshape(appndata,(6,3,441))
jitter = [0,1,3,5,7,9]
fig, axes = plt.subplots(nrows=2, ncols=3, 
                        figsize=([12, 9]), constrained_layout=True,sharex=True,sharey=True)
i=0
for ax in axes.flat:
    im =  ax.hexbin(appndata[i][0],appndata[i][1],C=appndata[i][2],gridsize=18, vmin=0,vmax=1.8*10**11)
    ax.set_title('gauss(0,%d)'%jitter[i])
    i+=1
fig.colorbar(im, ax=axes.ravel().tolist(),label='amplitude')
fig.supxlabel('Rit pixle',fontsize=20)
fig.supylabel('Rit pixel',fontsize=20)
plt.show()
