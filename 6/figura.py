import os

import vdWColumn as vdw

import vdWColumn.postLBRun as post

import matplotlib.pyplot as plt

import numpy as np




# van Der Waals properties

b = 4.0

plt.style.use('../custom.mplstyle')


# Move over Caso folders

for i in range(4):


    fn = "/users/fogliate/LBRun/vdWColumn/Berberan-Santos_et_al_2002/CasoG/Caso{}".format(i)

    if os.path.exists( fn ):

        rho = post.scalarProfile( fn, 'rho', time = 'latest' )

        with open('rho_{}'.format(i),'w') as f:

            for r in rho:

                f.write('{}\n'.format(r))

        
        
    rho = np.loadtxt( 'rho_{}'.format(i) )

    intm, ll, rl = post.interphase( rho, width = 0.05 )                
        
    plt.plot([ z/(len(rho)-1) for z in range(len(rho))], rho * 3.0 * b, label = "{} l.u".format(len(rho) - 1))   

    


# Solucion analitica

Er, Cg, Cl, Ei, Tr = vdw.rhoNonUniformLambda( Tt = 0.99, Tb = 0.99 )

sp = 250

plt.plot( Er[Ei::-sp]/Er[-1], Cl[Ei::-sp], linestyle = 'None',  marker = 'o', mfc = 'None')

plt.plot( Er[Ei::sp]/Er[-1], Cg[Ei::sp], linestyle = 'None',  marker = 'o', mfc = 'None')


    

# Labels

plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

plt.xlabel(r'$z \, / \, H$')

plt.legend(loc='best')        

plt.savefig( '6.png', format='png', dpi=600 )
