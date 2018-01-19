import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np



# Solucion con LBM

file1 = np.loadtxt( 'BS/c_bar_1.500.dat', unpack = True )
file2 = np.loadtxt( 'BS/c_bar_1.000.dat', unpack = True )
file3 = np.loadtxt( 'BS/c_bar_0.500.dat', unpack = True )
file4 = np.loadtxt( 'c_bar_1.500.dat', unpack = True )
file5 = np.loadtxt( 'c_bar_1.000.dat', unpack = True )
file6 = np.loadtxt( 'c_bar_0.500.dat', unpack = True )


plt.style.use('custom') 

sp = 150

# plt.plot( 1000*file2[0][::-sp],
#           file2[1][::-sp],
#           linestyle = 'None',
#           color = 'k',
#           marker = 'o',
#           mfc = 'None')

# plt.plot( 1000*file3[0][::sp],
#           file3[1][::sp],
#           linestyle = 'None',
#           color = 'k',
#           marker = 'o',
#           mfc = 'None')

# plt.plot( 1000*file4[0][::-sp],
#           file4[1][::-sp],
#           linestyle = 'None',
#           color = 'k',
#           marker = 'o',
#           mfc = 'None')

# plt.plot( 1000*file5[0][::sp],
#           file5[1][::sp],
#           linestyle = 'None',
#           color = 'k',
#           marker = 'o',
#           mfc = 'None')

# plt.plot( 1000*file6[0][::-sp],
#           file6[1][::-sp],
#           linestyle = 'None',
#           color = 'k',
#           marker = 'o',
#           mfc = 'None')

# plt.plot( 1000*file7[0][::sp],
#           file7[1][::sp],
#           linestyle = 'None',
#           color = 'k',
#           marker = 'o',
#           mfc = 'None')



plt.plot( file1[0], file1[3], label = r'$\bar{c} = 1.5$')

plt.plot( file2[0], file2[3], label = r'$\bar{c} = 1.0$')

plt.plot( file3[0], file3[3], label = r'$\bar{c} = 0.5$')

plt.plot( file4[1],
          file4[2]/300,
          linestyle = 'None',
          color = 'k',
          marker = 'o',
          mfc = 'None',
          label =  r'$\bar{c}_{lb} = 1.5$')

plt.plot( file5[1],
          file5[2]/300,
          linestyle = 'None',
          color = 'k',
          marker = '^',
          mfc = 'None',
          label =  r'$\bar{c}_{lb} = 1.0$')

plt.plot( file6[1],
          file6[2]/300,
          linestyle = 'None',
          color = 'k',
          marker = 's',
          mfc = 'None',
          label =  r'$\bar{c}_{lb} = 0.5$')


# Labels

plt.xlabel('$T_r$')

plt.ylabel('Liquid volume fraction')

# plt.legend(loc='best')        

plt.savefig( '8.png', format='png', dpi=600 )
