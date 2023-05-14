import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import mplhep
mplhep.style.use('ATLAS')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
data=np.load('specIdx_deg_88_150MHZ.npy',allow_pickle=True)
data=data[1:,:]
plt.figure(dpi=150)
for i in range(1,len(data)):
    plt.errorbar(data[i,1],data[i,2],yerr=data[i,3],color=cm.nipy_spectral((data[0:,0][i]-min(data[0:,0]))/(max(data[0:,0])+20-min(data[0:,0]))),label='%.2f'%data[i,0],marker='o',capsize=2)
plt.ticklabel_format(axis='y', style='sci', scilimits=(2,2))
plt.grid( linestyle='--', linewidth=1)
plt.xlabel('x [m]/d$_{750}$',fontsize=20)
plt.ylabel('b$_{%d MHz}[GHz]^{-1}$'%(50),fontsize=20)
plt.legend( prop={'size': 15},title='X$_{max}$ $g/cm^2$',title_fontsize=17,bbox_to_anchor=(1, 1.1), loc='upper left')
#plt.xlim(-2,2)
#plt.savefig('deg_50a.png')
plt.show()