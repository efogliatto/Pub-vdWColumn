import os

import vdWColumn as vdw

import vdWColumn.postLBRun as post

import matplotlib.pyplot as plt

import numpy as np




# van Der Waals properties

Er_max = 1e-03

b = 4.0

plt.style.use('../custom.mplstyle')


# Move over Caso folders

sigmaList = [0.0125, 0.125, 1.25]

for i,sigma in zip( range(3), sigmaList ):


    fn = "/users/fogliate/LBRun/vdWColumn/fixedT/CasoD/Caso{}".format(i)

    if os.path.exists( fn ):

        rho = post.scalarProfile( fn, 'rho', time = 'latest' )

        with open('rho_{}'.format(i),'w') as f:

            for r in rho:

                f.write('{}\n'.format(r))

        
        
    rho = np.loadtxt( 'rho_{}'.format(i) )

    intm, ll, rl = post.interphase( rho, width = 0.05 )

    label = '$\sigma = $' + '{}'.format(sigma)

    plt.plot([ z/(len(rho)-1) for z in range(len(rho))], rho * 3.0 * b, label = label)   

    

    
# Solucion analitica

Er, Cg, Cl, Ei, Tr = vdw.rhoNonUniformLambda( Tt = 0.99, Tb = 0.8 )

sp = 100

plt.plot( Er[Ei::-sp]/Er[-1], Cl[Ei::-sp], linestyle = 'None',  marker = 'o', mfc = 'None')

plt.plot( Er[Ei::sp]/Er[-1], Cg[Ei::sp], linestyle = 'None',  marker = 'o', mfc = 'None')    


    

# Labels

plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

plt.xlabel(r'$z \, / \, H$')

plt.xlim((0.3,0.6))

plt.legend(loc='best')        

plt.savefig( '12.png', format='png', dpi=600 )
