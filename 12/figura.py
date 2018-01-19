import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np




# van Der Waals properties

Er_max = 1e-03

b = 4.0

plt.style.use('../custom.mplstyle')


# Move over Caso folders

sigmaList = [0.0125, 0.125, 1.25]

for i,sigma in zip( range(3), sigmaList ):
   
    rho = post.scalarProfile( "/users/fogliate/LBRun/vdWColumn/fixedT/CasoD/Caso{}/processor0/2000000/rho".format(i), step = 3, offset = 1 )

    intm, ll, rl = post.interphase( rho, width = 0.05 )

    label = '$\sigma = $' + '{}'.format(sigma)
    
    plt.plot([ z/(len(rho)-1) for z in range(len(rho))], rho * 3.0 * b, label = label)   

    


# Solucion analitica

er, cr = np.loadtxt( "Tr_0.990_0.800_cbar_1.000.dat", unpack = True )

intm = post.analiticInterphase( er, cr )



# Split profiles for better plotting

erl, crl, erv, crv = [], [], [], []

for i in range( len(er) -1 ):

    if np.isclose(er[i], er[i+1]):

        erl = er[:i]

        erg = er[i+1:]

        crl = cr[:i]

        crg = cr[i+1:]        


erl = erl[::-100]

crl = crl[::-100]

erg = erg[::100]

crg = crg[::100]


plt.plot( [  z/er[-1] for z in erl  ],
          crl,
          label = 'Berberan-Santos',
          linestyle = 'None',
          marker = 'o',
          mfc = 'None')

plt.plot( [  z/er[-1] for z in erg  ],
          crg,
          linestyle = 'None',
          marker = 'o',
          mfc = 'None')        

    

# Labels

plt.ylabel(r'$\rho_r$')

plt.xlabel(r'$z \, / \, H$')

plt.xlim((0.3,0.6))

plt.legend(loc='best')        

plt.savefig( '12.png', format='png', dpi=600 )
