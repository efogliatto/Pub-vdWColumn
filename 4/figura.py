import os

import vdWColumn as vdw

import vdWColumn.postLBRun as post

import matplotlib.pyplot as plt

import numpy as np





# van Der Waals properties

b = 4.0


with plt.style.context('../custom.mplstyle'):

    
    plt.figure()
    
    
    # Move over Caso folders

    for i in range(4):


        fn = "/users/fogliate/LBRun/vdWColumn/Berberan-Santos_et_al_2002/CasoH/Caso{}".format(i)

        if os.path.exists( fn ):

            rho = post.scalarProfile( fn, 'rho', time = 'latest' )

            with open('rho_{}'.format(i),'w') as f:

                for r in rho:

                    f.write('{}\n'.format(r))

                    
    
        rho = np.loadtxt( 'rho_{}'.format(i) )

        intm, ll, rl = post.interphase( rho, width = 0.05 )

        plabel = "$E_{r_{max}}=10^{" + "{}".format(-1-i) + "}$"
        
        plt.plot( [  (z-intm)/(len(rho)-1) for z in range( len(rho) )  ],  rho * 3.0 * b, label = plabel)
        


        

    # Labels

    plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

    plt.xlabel('Reduced height at the vapor-liquid boundary')

    plt.xlim((-0.4,0.4))

    plt.legend(loc='best')

    plt.savefig( '4.png', format='png', dpi=300 )    
