import vdWColumn as vdw

import vdWColumn.postLBRun as post

import matplotlib.pyplot as plt

import numpy as np



plt.style.use('../custom.mplstyle')



# Solucion con LBM

file4 = np.loadtxt( 'c_bar_1.500.dat', unpack = True )

file5 = np.loadtxt( 'c_bar_1.000.dat', unpack = True )

file6 = np.loadtxt( 'c_bar_0.500.dat', unpack = True )

plt.plot( file4[1], file4[2]/300,  linestyle = 'None',  color = 'k',  marker = 'o',  mfc = 'None', label =  r'$\bar{c}_{lb} = 1.5$')

plt.plot( file5[1],  file5[2]/300,  linestyle = 'None',  color = 'k', marker = '^',  mfc = 'None', label =  r'$\bar{c}_{lb} = 1.0$')

plt.plot( file6[1], file6[2]/300, linestyle = 'None', color = 'k',  marker = 's',  mfc = 'None', label =  r'$\bar{c}_{lb} = 0.5$')





sp = 150



file1 = np.loadtxt( 'BS/c_bar_1.500.dat', unpack = True )
file2 = np.loadtxt( 'BS/c_bar_1.000.dat', unpack = True )
file3 = np.loadtxt( 'BS/c_bar_0.500.dat', unpack = True )

plt.plot( file1[0], file1[3], label = r'$\bar{c} = 1.5$', linestyle = '-')

plt.plot( file2[0], file2[3], label = r'$\bar{c} = 1.0$', linestyle = '-')

plt.plot( file3[0], file3[3], label = r'$\bar{c} = 0.5$', linestyle = '-')



# Labels

plt.xlabel(r'$T_r$', rotation='horizontal', labelpad=15)

plt.ylabel(r'$z \, / \, H$')

# plt.legend(loc='best')        

plt.savefig( '8.png', format='png', dpi=600 )
