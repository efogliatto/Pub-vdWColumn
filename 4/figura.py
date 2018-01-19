import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np





# van Der Waals properties

b = 4.0


with plt.style.context('../custom.mplstyle'):

    
    plt.figure()
    
    
    # Move over Caso folders

    for i in range(4):
    
        rho = post.scalarProfile( "/users/fogliate/LBRun/vdWColumn/Berberan-Santos_et_al_2002/CasoH/Caso{}/processor0/2000000/rho".format(i), step = 3, offset = 1 )

        intm, ll, rl = post.interphase( rho, width = 0.05 )

        plabel = "$E_{r_{max}}=10^{" + "{}".format(-1-i) + "}$"
        
        plt.plot( [  (z-intm)/(len(rho)-1) for z in range( len(rho) )  ],  rho * 3.0 * b, label = plabel)


        

    # Labels

    plt.ylabel(r'$\rho_r$')

    plt.xlabel('Reduced height at the vapor-liquid boundary')

    plt.xlim((-0.4,0.4))

    plt.legend(loc='best')

    # plt.savefig( 'c_vs_z_Er.svg', format='svg', dpi=1200 )

    # plt.savefig( 'c_vs_z_Er_dpi1200.png', format='png', dpi=1200 )

    plt.savefig( '4.png', format='png', dpi=300 )    

    # plt.show()




# with plt.style.context('custom'):

    
#     plt.figure()

    
#     # Move over analitica files

#     for i in range(4):
    
#         er, cr = np.loadtxt( "analitica/Er_{:.5f}_cbar_1.000.dat".format(10**(-1-i)), unpack = True )

#         intm = post.analiticInterphase( er, cr )
    
#         plabel = "$E_{r_{max}}=10^{" + "{}".format(-1-i) + "}$"
        
#         plt.plot( [  (z-intm)/er[-1] for z in er  ],  cr, label = plabel)


        

#     # Labels

#     plt.ylabel('$c$')

#     plt.xlabel('Reduced height at the vapor-liquid boundary')

#     plt.xlim((-0.4,0.4))

#     plt.legend(loc='best')

#     # plt.savefig( 'c_vs_z_Er_analitica.svg', format='svg', dpi=1200 )

#     plt.savefig( 'c_vs_z_Er_analitica_dpi1200.png', format='png', dpi=1200 )

#     plt.savefig( 'c_vs_z_Er_analitica.png', format='png', dpi=300 )

#     # plt.show()  
    
