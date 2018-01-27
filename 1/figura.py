import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np



# Solucion con LBM

sigma_0 = np.loadtxt( "sigma_1.25.dat", unpack = True )

sigma_1 = np.loadtxt( "sigma_0.125.dat", unpack = True )

sigma_2 = np.loadtxt( "sigma_0.0125.dat", unpack = True )


# Solucion analitica

vdW = np.loadtxt( "vdW.dat", unpack = True )


plt.style.use('../custom.mplstyle') 

plt.plot( sigma_0[4],
          sigma_0[1],
          label = r'$\sigma=1.25$',
          linestyle = 'None',
          color = 'k',
          marker = 'o',
          mfc = 'None')

plt.plot( sigma_0[5],
          sigma_0[1],
          linestyle = 'None',
          color = 'k',
          marker = 'o',
          mfc = 'None')

plt.plot( sigma_1[4],
          sigma_1[1],
          label = r'$\sigma=0.125$',
          linestyle = 'None',
          color = 'k',
          marker = '^',
          mfc = 'None')

plt.plot( sigma_1[5],
          sigma_1[1],
          linestyle = 'None',
          color = 'k',
          marker = '^',
          mfc = 'None')

plt.plot( sigma_2[4],
          sigma_2[1],
          label = r'$\sigma=0.0125$',
          linestyle = 'None',
          color = 'k',
          marker = 's',
          mfc = 'None')

plt.plot( sigma_2[5],
          sigma_2[1],
          linestyle = 'None',
          color = 'k',
          marker = 's',
          mfc = 'None')


plt.plot( vdW[1], vdW[0], label = 'van der Waals')
plt.plot( vdW[2], vdW[0], linestyle = '-')
        


# Labels

plt.ylabel('$T_r$', rotation='horizontal', labelpad=15)

plt.xlabel(r'$\rho_r$')

# plt.xlim((-0.4,0.4))

# plt.legend(loc='best')        

plt.savefig( '1.png', format='png', dpi=600 )

# plt.show()
