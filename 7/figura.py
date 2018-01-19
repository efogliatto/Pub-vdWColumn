import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np





# van Der Waals properties

Er_max = 1e-01

b = 4.0

plt.style.use('custom')


# Move over Caso folders

for i in range(4):

    rho = post.scalarProfile( "/users/fogliate/LBRun/vdWColumn/Berberan-Santos_et_al_2002/CasoI/Caso{}/processor0/2000000/rho".format(i), step = 3, offset = 1 )

    intm, ll, rl = post.interphase( rho, width = 0.05 )

    # plt.plot([ (z-intm)/(len(rho)-1) for z in range(len(rho))], rho * 3.0 * b, label = "{} l.u".format(len(rho) - 1))
    plt.plot([ z/(len(rho)-1) for z in range(len(rho))], rho * 3.0 * b, label = "{} l.u".format(len(rho) - 1))



# Solucion analitica

er, cr = np.loadtxt( "analitica/Er_0.10000_cbar_1.000.dat", unpack = True )

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


# plt.plot( [  (z-intm)/er[-1] for z in erl  ],
#           crl,
#           label = 'Berberan-Santos',
#           linestyle = 'None',
#           marker = 'o',
#           mfc = 'None')

# plt.plot( [  (z-intm)/er[-1] for z in erg  ],
#           crg,
#           linestyle = 'None',
#           marker = 'o',
#           mfc = 'None')
        
plt.plot( [  z/er[-1] for z in erl  ],
          crl,
          # label = 'Berberan-Santos',
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

# plt.xlim((-0.4,0.4))

plt.legend(loc='best')        

plt.savefig( '7.png', format='png', dpi=600 )