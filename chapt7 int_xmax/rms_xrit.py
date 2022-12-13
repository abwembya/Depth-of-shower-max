import numpy as np
from matplotlib import cbook
import matplotlib.colors
import matplotlib.pyplot as plt
import mplhep as hep
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
hep.style.use("ATLAS")

#plot a 3X2 grid of plots of the spread/calculates the rms  and plots the rms vs the sigma of the plot
gauss=[[0,0],[0,1],[0,3],[0,5],[0,7],[0,9]]
#xxmaxs6 = np.genfromtxt(r"C:\Users\Echo!\OneDrive - campus.mephi.ru\Documents\proton\xmaxs.csv",delimiter=",", dtype=float)
xxmaxs6 = np.genfromtxt("xmaxs",delimiter=",", dtype=float)
s4=int(len(np.asarray(xxmaxs6))/6)

sigmas0=xxmaxs6[0:s4]
sigmas1=xxmaxs6[s4:s4*2]
sigmas3=xxmaxs6[s4*2:s4*3]
sigmas5=xxmaxs6[s4*3:s4*4]
sigmas7=xxmaxs6[s4*4:s4*5]
sigmas9=xxmaxs6[s4*5:s4*6]
subplots = [sigmas0,sigmas1,sigmas3,sigmas5,sigmas7,sigmas9]
fig, axes = plt.subplots(nrows=2, ncols=3, 
                        figsize=([12, 9]), constrained_layout=True,sharex=True,sharey=True)
j=0
zmax=0
zmin=0
rms=[]
for ax in axes.flat:
        m, b = np.polyfit(subplots[j][0::2], subplots[j][1::2], deg=1)
        scatter=subplots[j][1::2]-(m*subplots[j][0::2]+b)
        im=ax.scatter(subplots[j][0::2],scatter)
        rms.append(np.sqrt(np.mean(scatter**2)))
        #ax.axline(xy1=(0, b), slope=m, c='b' ,label=f'$y = {m:.2f}x {b:+.2f}$',alpha=0.2)
        #ax.text(0.05, 0.95, f'$y = {m:.2f}x {b:+.2} $', transform=ax.transAxes, fontsize=14, verticalalignment='top')
        ax.set_title('gauss(0,%d)'%gauss[j][1])
        ax.grid()
        j+=1
#fig.colorbar(im, ax=axes.ravel().tolist(),label="|x$_{max}$ - x$_{max} rit$|")
fig.supxlabel('x$_{max} ~[g/cm^2]$',fontsize=30)
fig.supylabel('Spread',fontsize=30)
plt.savefig('rms_xrit.png')
plt.show()


plt.figure( dpi=100)
plt.plot([0,1,3,5,7,9],rms,'o')
plt.xlim(-0.2, 10)
plt.xlabel('sigma $\sigma_t$ [ns]')
plt.ylabel('RMS of rit spread')
plt.grid( linestyle='--', linewidth=0.5)
plt.savefig('rms.png')
plt.show()
