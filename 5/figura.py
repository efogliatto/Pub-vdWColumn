import os

import vdWColumn as vdw

import vdWColumn.postLBRun as post

import matplotlib.pyplot as plt

import numpy as np





# van Der Waals properties

b = 4.0



with plt.style.context('../custom.mplstyle'):

    
    plt.figure()

    
    # Move over analitica files

    for et in [1.0e-04, 1.0e-03, 1.0e-02, 1.0e-01]:

        Er, Cg, Cl, Ei, Tr = vdw.rhoNonUniformLambda( Tt = 0.99, Tb = 0.99, Et = et )
    
        plabel = "$E_{r_{max}}=" + "{:.0e}$".format(et)
        
        plt.plot( np.concatenate( [ [(z-Er[Ei]) / et  for z in Er[:Ei]], [(z-Er[Ei]) / et  for z in Er[Ei:]] ]  ) ,
                  np.concatenate( [ Cl[:Ei], Cg[Ei:] ] ),
                  label = plabel)

        

    # Labels

    plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

    plt.xlabel('Reduced height at the vapor-liquid boundary')

    plt.xlim((-0.4,0.4))

    plt.legend(loc='best')

    plt.savefig( '5.png', format='png', dpi=600 )

    
