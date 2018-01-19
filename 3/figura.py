import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np



# Solucion con LBM

file1 = np.loadtxt( 'LB.dat', unpack = True )


# Solucion de Berberan-Santos

file2 = np.loadtxt( 'Tr_0.990_0.990_cbar_1.000.dat', unpack = True )
file3 = np.loadtxt( 'Tr_0.990_0.990_cbar_1.000_gas.dat', unpack = True )
file4 = np.loadtxt( 'Tr_0.700_0.700_cbar_1.000.dat', unpack = True )
file5 = np.loadtxt( 'Tr_0.700_0.700_cbar_1.000_gas.dat', unpack = True )
file6 = np.loadtxt( 'Tr_0.500_0.500_cbar_1.000.dat', unpack = True )
file7 = np.loadtxt( 'Tr_0.500_0.500_cbar_1.000_gas.dat', unpack = True )


plt.style.use('custom') 

sp = 150

plt.plot( 1000*file2[0][::-sp],
          file2[1][::-sp],
          linestyle = 'None',
          color = 'k',
          marker = 'o',
          mfc = 'None')

plt.plot( 1000*file3[0][::sp],
          file3[1][::sp],
          linestyle = 'None',
          color = 'k',
          marker = 'o',
          mfc = 'None')

plt.plot( 1000*file4[0][::-sp],
          file4[1][::-sp],
          linestyle = 'None',
          color = 'k',
          marker = '^',
          mfc = 'None')

plt.plot( 1000*file5[0][::sp],
          file5[1][::sp],
          linestyle = 'None',
          color = 'k',
          marker = '^',
          mfc = 'None')

plt.plot( 1000*file6[0][::-sp],
          file6[1][::-sp],
          linestyle = 'None',
          color = 'k',
          marker = 's',
          mfc = 'None')

plt.plot( 1000*file7[0][::sp],
          file7[1][::sp],
          linestyle = 'None',
          color = 'k',
          marker = 's',
          mfc = 'None')



plt.plot( file1[0]/3000, file1[1]*12, label = r'$T_r=0.99$', linestyle = '-')

plt.plot( file1[0]/3000, file1[2]*12, label = r'$T_r=0.70$', linestyle = '-')

plt.plot( file1[0]/3000, file1[3]*12, label = r'$T_r=0.50$', linestyle = '-')

        


# Labels

plt.ylabel(r'$\rho_r$')

# plt.xlabel('$E_r \, / \, E_{r_{max}}$')
plt.xlabel(r'$z \, / \, H$')

# plt.legend(loc='best')      



plt.savefig( '3.png', format='png', dpi=600 )

# plt.show()
