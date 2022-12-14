import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import mplhep
mplhep.style.use('ATLAS')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
deg_88a=np.load('deg_88a.npy',allow_pickle=True)#input data
plt.figure(dpi=150)
for i in range(1,deg_88a.shape[0]):
    plt.plot(deg_88a[i,1],deg_88a[i,2],color=cm.nipy_spectral((deg_88a[0:,0][i]-min(deg_88a[0:,0]))/(max(deg_88a[0:,0])+20-min(deg_88a[0:,0]))) ,label='%.2f'%deg_88a[i,0],marker='o')  
plt.legend( prop={'size': 11},title='Xmax',title_fontsize=13,bbox_to_anchor=(1, 1.1), loc='upper left')
plt.xlabel('Cherenkov redii [au]',fontsize=13)
plt.ylabel('slope$_{50MHz}$ [$\mu V$/m/GHz]',fontsize=13)
plt.grid( linestyle='--', linewidth=0.5 ,color='grey',alpha=0.5)
plt.xlim(-2,2)
#plt.savefig('deg_50a.png')
plt.show()