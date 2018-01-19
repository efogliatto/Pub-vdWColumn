import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np





# van Der Waals properties

b = 4.0



with plt.style.context('custom'):

    
    plt.figure()

    
    # Move over analitica files

    for i in range(4):
    
        er, cr = np.loadtxt( "analitica/Er_{:.5f}_cbar_1.000.dat".format(10**(-1-i)), unpack = True )

        intm = post.analiticInterphase( er, cr )
    
        plabel = "$E_{r_{max}}=10^{" + "{}".format(-1-i) + "}$"
        
        plt.plot( [  (z-intm)/er[-1] for z in er  ],  cr, label = plabel)


        

    # Labels

    plt.ylabel(r'$\rho_r$')

    plt.xlabel('Reduced height at the vapor-liquid boundary')

    plt.xlim((-0.4,0.4))

    plt.legend(loc='best')

    plt.savefig( '5.png', format='png', dpi=600 )

    
