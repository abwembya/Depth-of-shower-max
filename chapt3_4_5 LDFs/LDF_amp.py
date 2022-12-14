import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import mplhep
import os
mplhep.style.use('ATLAS')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

plt.figure(dpi=100)
deg_50=np.load('deg_82.npy',allow_pickle=True)
for i in range(1,deg_50.shape[0]):
    plt.plot(deg_50[i,1],deg_50[i,2],color=cm.nipy_spectral((deg_50[0:,0][i]-min(deg_50[0:,0]))/(max(deg_50[0:,0])+20-min(deg_50[0:,0]))) ,label='%.2f'%deg_50[i,0],marker='o')
plt.legend( prop={'size': 11},title='Xmax',title_fontsize=13,bbox_to_anchor=(1, 1.1), loc='upper left')
plt.xlabel('Cherenkov redii [au]',fontsize=13)
plt.ylabel('amp [$\mu$V/m]',fontsize=13)
plt.grid( linestyle='--', linewidth=0.5 ,color='grey',alpha=0.5)
plt.xlim(-2,2)
plt.show()