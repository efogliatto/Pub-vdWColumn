import os

import vdWColumn as vdw

import matplotlib.pyplot as plt

import numpy as np




# van Der Waals properties

Er_max = 1e-03

b = 4.0

plt.style.use('../custom.mplstyle')


# # Move over Caso folders

# for i in range(4):

#     fn = "/users/fogliate/LBRun/vdWColumn/fixedT/CasoC/Caso{}/processor0/2000000/rho".format(i)

#     if os.path.exists( fn ):

#         os.system("cp {} rho_{}".format(fn,i))
        
    
#     rho = post.scalarProfile( "rho_{}".format(i), step = 3, offset = 1 )

#     intm, ll, rl = post.interphase( rho, width = 0.05 )
        
#     plt.plot([ z/(len(rho)-1) for z in range(len(rho))], rho * 3.0 * b, label = "{} l.u".format(len(rho) - 1))   

    


Er, C_g, C_l, Ei = vdw.rhoNonUniformLambda( Tb = 0.8 )



# plt.plot( [  z/er[-1] for z in erl  ],
#           crl,
#           # label = 'Berberan-Santos',
#           linestyle = 'None',
#           marker = 'o',
#           mfc = 'None')

# plt.plot( [  z/er[-1] for z in erg  ],
#           crg,
#           linestyle = 'None',
#           marker = 'o',
#           mfc = 'None')        

    

# # Labels

# plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

# plt.xlabel(r'$z \, / \, H$')

# plt.xlim((0.3,0.6))

# plt.legend(loc='best')        

# plt.savefig( '11.png', format='png', dpi=600 )
