import os

import matplotlib.pyplot as plt

import numpy as np





plt.style.use('../custom.mplstyle')

data = np.loadtxt('Tr_0.900.dat')

plt.plot( data[:,1], data[:,2] / 300., label = 'LB', linestyle = 'None', marker = 'o', mfc = 'None')



# Solucion analitica

vdw = np.loadtxt( "Inter_cbar_Tr_0.9.dat" )

plt.plot( vdw[:,0], vdw[:,1], label = 'Berberan-Santos' )



# Labels

plt.xlabel(r'Mean $\rho_r$')

plt.ylabel('Liquid volume fraction')

plt.xlim((0.5,1.6))

plt.ylim((0.1,0.9))

# plt.legend(loc='best')        

plt.savefig( '9.png', format='png', dpi=600 )

# plt.show()
