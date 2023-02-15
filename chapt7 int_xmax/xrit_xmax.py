import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
hep.style.use("ATLAS")
#plot the xrit vs xmax for differet sigma 

xxmaxs6 = np.genfromtxt("xmaxs",delimiter=",", dtype=float)
gauss=[[0,0],[0,1],[0,3],[0,5],[0,7],[0,9]]
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
for ax in axes.flat:
        im=ax.scatter(subplots[j][0::2],subplots[j][1::2])
        m, b = np.polyfit(subplots[j][0::2], subplots[j][1::2], deg=1)
        ax.axline(xy1=(0, b), slope=m, c='b' ,label=f'$y = {m:.2f}x {b:+.2f}$',alpha=0.2)
        ax.text(0.05, 0.95, f'$y = {m:.2f}x {b:+.2} $', transform=ax.transAxes, fontsize=14, verticalalignment='top')
        ax.set_title('Jitter=%d ns'%gauss[j][1])
        ax.grid()
        if max(np.abs(subplots[j][::2]-subplots[j][::-2][::-1]))>zmax:
                zmax=max(np.abs(subplots[j][::2]-subplots[j][::-2][::-1]))
        if min(np.abs(subplots[j][::2]-subplots[j][::-2][::-1]))<zmin:
                zmin=min(np.abs(subplots[j][::2]-subplots[j][::-2][::-1]))
        j+=1
#fig.colorbar(im, ax=axes.ravel().tolist(),label="|x$_{max}$ - x$_{max} rit$|")
plt.ylim(500, 1000)
plt.xlim(600, 1000)
fig.supxlabel('X$_{\mathrm{max}} ~[g/cm^2]$',fontsize=30)
fig.supylabel('X$_{\mathrm{rit}}$',fontsize=30)
plt.savefig('xmaxs.png')
plt.show()