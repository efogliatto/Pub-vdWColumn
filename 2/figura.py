import vdWColumn as vdw

import matplotlib.pyplot as plt

import numpy as np




plt.style.use('../custom.mplstyle')


# Solucion con LBM

file1 = np.loadtxt( 'LB.dat', unpack = True )

plt.plot( file1[0]/300, file1[1]*12, label = r'$T_r=0.99$', linestyle = '-')

plt.plot( file1[0]/300, file1[2]*12, label = r'$T_r=0.70$', linestyle = '-')

plt.plot( file1[0]/300, file1[3]*12, label = r'$T_r=0.50$', linestyle = '-')




# Solucion de Berberan-Santos

Tlist = [0.99, 0.7, 0.5]

sp = 250

for T in Tlist:

    Er, Cg, Cl, Ei, Tr = vdw.rhoNonUniformLambda( Tt = T, Tb = T )

    plt.plot( 1000*Er[Ei::-sp], Cl[Ei::-sp], linestyle = 'None', color = 'k',  marker = 'o',  mfc = 'None')

    plt.plot( 1000*Er[Ei::sp], Cg[Ei::sp], linestyle = 'None', color = 'k',  marker = 'o',  mfc = 'None')


        


# Labels

plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

plt.xlabel(r'$z \, / \, H$')

plt.savefig( '2.png', format='png', dpi=600 )
