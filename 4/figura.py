import os

import vdWColumn as vdw

import vdWColumn.postLBRun as post

import matplotlib.pyplot as plt

import numpy as np





# van Der Waals properties

b = 4.0

mkstyle = ['o','^','s','*','x']


with plt.style.context('../custom.mplstyle'):

    
    plt.figure()
    
    
    # Move over Caso folders

    for i, et in zip( range(3), [1.0e-01, 1.0e-02, 1.0e-03, 1.0e-04] ):


        # Solucion LB
        
        fn = "/users/fogliate/LBRun/vdWColumn/Berberan-Santos_et_al_2002/CasoK/Caso{}".format(i)

        if os.path.exists( fn ):

            rho = post.scalarProfile( fn, 'rho', time = 'latest' )

            with open('rho_{}'.format(i),'w') as f:

                for r in rho:

                    f.write('{}\n'.format(r))

                    
    
        rho = np.loadtxt( 'rho_{}'.format(i) )

        intm, ll, rl = post.interphase( rho, width = 0.05 )

        # plabel = "$E_r=10^{" + "{}".format(-1-i) + "}$"
        
        plt.plot( [  (z-intm)/(len(rho)-1) for z in range( len(rho) )  ],  rho * 3.0 * b, linestyle = '-')




        # Solucion analitica

        sp = 200
        
        Er, Cg, Cl, Ei, Tr = vdw.rhoNonUniformLambda( Tt = 0.99, Tb = 0.99, Et = et )
        
        plt.plot( [ (z-Er[Ei]) / et  for z in Er[Ei::-sp] ], Cl[Ei::-sp], linestyle = 'None', color = 'k',  marker = mkstyle[i],  mfc = 'None')

        plt.plot( [ (z-Er[Ei]) / et  for z in Er[Ei::sp] ], Cg[Ei::sp], linestyle = 'None', color = 'k',  marker = mkstyle[i],  mfc = 'None')        
                  
        


        

    # Labels

    plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

    plt.xlabel(r'$(z - z_0)\, / \,H$')

    plt.xlim((-0.4,0.4))

    # plt.legend(loc='best')

    plt.savefig( '4.png', format='png', dpi=300 )    
