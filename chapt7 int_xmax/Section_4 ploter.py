
import numpy as np
from matplotlib import cbook
import matplotlib.colors
import matplotlib.pyplot as plt
import mplhep as hep
import os
hep.style.use("ATLAS")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#plots the integrated power in the pixels as a function of the sigma 

xx,yy,p=np.load('rit_pixle_2000.npy',allow_pickle=True)
plt.figure(dpi=150,figsize=(9,8.5))
plt.scatter(xx,yy,c=p/max(p),s=40,marker='H',cmap='inferno')
plt.xlabel("Distance [m]",size=25)
plt.ylabel("Distance [m]",size=25)
#plt.colorbar(label='integrated power (a.u.)', pad=0.04)
plt.colorbar().set_label(label='Normalised Inergrated Power',size=20)
plt.xlim(-2000,2000)
plt.ylim(-2000,2000)
# plt.show()
########################################################################################################################

long_data=np.load('long_data2.npy',allow_pickle=True)
plt.figure(dpi=150,figsize=(7,6))
plt.plot(long_data[:long_data.shape[0]//3,1],long_data[:long_data.shape[0]//3,3]/max(long_data[:long_data.shape[0]//3,3]),label='689.85g/cm$^2$',c='blue',linestyle=':')
plt.plot(long_data[long_data.shape[0]//3:2*long_data.shape[0]//3,1],long_data[long_data.shape[0]//3:2*long_data.shape[0]//3,3]/max(long_data[long_data.shape[0]//3:2*long_data.shape[0]//3,3]),label='917.28 g/cm$^2$',c='r',linestyle='--')
plt.plot(long_data[2*long_data.shape[0]//3:,1],long_data[2*long_data.shape[0]//3:,3]/max(long_data[2*long_data.shape[0]//3:,3]),label='1024.59 g/cm$^2$',c='k',linestyle='-.')
plt.ylabel('Normalised Intergrated Power',size=20)
plt.xlabel('X [g/cm$^2]$',size=20)
plt.grid( linestyle='--',alpha=0.5)
plt.ylim(0,)
plt.xlim(200,1800)
plt.legend(fontsize=12,loc='upper right',frameon=True,framealpha=0.5,title=r'X$\rm_{max}$')
plt.show()



###########################################################

xxmax=np.load('xrit vs xmax.npy')
m,b=np.polyfit(xxmax[::2],xxmax[1::2],1)    
plt.figure(dpi=100)
plt.scatter(xxmax[::2],xxmax[1::2],color='red',marker='o',s=100)
plt.axline(xy1=(0, b), slope=m, c='b' ,label=f'$y = {m:.2f}x {b:+.2f}$',alpha=0.5,linewidth=3,ls='--')

plt.xlim(650,950)
plt.ylim(550,900)
plt.grid(ls="--" )
plt.title('Shower Depth Calibration Curve ',fontsize=20)
plt.ylabel(r'X$_{\rm {rit}}$ [g/cm$^2$]', ha='center', va='center',fontsize=18,labelpad=20)
plt.xlabel(r'X$_{\rm {max}}$(True) [g/cm$^2$]')
plt.legend(fontsize=15)
plt.show()
####################################################################

def calculate_error_propagation(X_max,X_rit, b, sigma_b, m, sigma_m):
    n = len(X_rit)
    # Calculate the expression S
    S = np.sqrt(np.mean((X_rit - b - m * X_max) ** 2))
    dS_dm = 1/n * sum(X_max*( b + m * X_max-X_rit))/S
    dS_db = 1/n *sum( 1*( b + m * X_max-X_rit))/S
    # Calculate the uncertainty in S
    sigma_S = np.sqrt((dS_db * sigma_b) ** 2 + (dS_dm * sigma_m) ** 2)
    return S, sigma_S

def calculate_S200_data(path):
    S_200 = np.array([])
    
    for j in range(9):
        xx = []
        yy = []
        S_100 = np.array([])
        data = np.loadtxt(f"{path}/xxmaxs100_{j}.txt", delimiter=',')

        for i in range(len(data)):
            [m, b], cov_mat = np.polyfit(data[i][0::2], data[i][1::2], deg=1, cov=True)
            sigma_m, sigma_b = np.sqrt(np.diag(cov_mat))
            S= calculate_error_propagation(data[i][0::2], data[i][1::2], b, sigma_b, m, sigma_m)[0]
            xx.append(data[i][0::2])
            yy.append(data[i][1::2])
            S_100 = np.append(S_100, S)
            
        xx = np.ravel(xx)
        yy = np.ravel(yy)
        [m, b], cov_mat = np.polyfit(xx, yy, deg=1, cov=True)
        sigma_m, sigma_b = np.sqrt(np.diag(cov_mat))
        S = calculate_error_propagation(xx, yy, b, sigma_b, m, sigma_m)[0]
        S_200 = np.append(S_200, [S, np.std(S_100)])

    return S_200

S_200 = calculate_S200_data("XritXmax/auger")
plt.errorbar(range(len(S_200)//2), S_200[0::2], yerr=S_200[1::2], fmt='o', label='30-80 MHz 1500m')
plt.fill_between(np.arange(len(S_200)//2), S_200[0::2]-S_200[1::2], S_200[0::2]+S_200[1::2], alpha=0.2)
S_200 = calculate_S200_data("XritXmax/grand")
plt.errorbar(range(len(S_200)//2), S_200[0::2], yerr=S_200[1::2], fmt='o', label='30-200 MHz 1500m')
plt.fill_between(np.arange(len(S_200)//2), S_200[0::2]-S_200[1::2], S_200[0::2]+S_200[1::2], alpha=0.2)
plt.legend( loc='upper left', numpoints = 1, frameon=False, fontsize=15)
plt.grid( linestyle='--', linewidth=1, alpha=0.5)
plt.xlabel(r'$\rm\sigma_{t}$ [ns]', fontsize=20)
plt.ylabel(r'$\rm\sigma_{Xmax}$[g/cm$^2$]', fontsize=20)
plt.xlim(0,len(S_200)//2-.5)
#plt.ylim(0,)
#plt.yscale('log')
plt.show()