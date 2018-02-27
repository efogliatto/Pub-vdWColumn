import vdWColumn as vdw

import numpy as np

import matplotlib.pyplot as plt




if __name__ == "__main__":

        
    # Solucion ya obtenida

    lbFiles = { '0.99' : np.loadtxt( 'Caso1.dat' ),
                '0.90' : np.loadtxt( 'Caso2.dat' ),
                '0.80' : np.loadtxt( 'Caso3.dat' ),
                '0.70' : np.loadtxt( 'Caso4.dat' ),
                '0.60' : np.loadtxt( 'Caso5.dat' ) }


    plt.style.use('../custom.mplstyle') 


    mkstyle = ['o','^','s','*','x']


    # Plot simulation files

    for key in sorted(lbFiles.keys(), reverse = True):

        plt.plot( lbFiles[key][:,0] / 3000., lbFiles[key][:,1] * 12., label = '$T_b = {}$'.format(key), linestyle = '-' )

    


    c_bar = 1.0

    Tt = 0.99

    sp = 250

    for T,mk in zip([0.99, 0.90, 0.80, 0.70, 0.60], mkstyle):

        if T > 0.95:
        
            Er, C_g, C_l, Ei, Tr = vdw.rhoNonUniformLambda( Tb = T, updateT = False )

        else:

            Er, C_g, C_l, Ei, Tr = vdw.rhoNonUniformLambda( Tb = T, updateT = True )
            

        plt.plot( Er[Ei::-sp] / 1e-03, C_l[Ei::-sp], linestyle = 'None', label = '$T_b = {}$'.format(key),  marker = mk,  mfc = 'None')

        plt.plot( Er[Ei::sp] / 1e-03, C_g[Ei::sp], linestyle = 'None', marker = mk,  mfc = 'None')


        
    # Labels

    plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

    plt.xlabel(r'$z \, / \, H$')

    plt.savefig( '10.png', format='png', dpi=600 )







# # Load data files

# lbFiles = { '0.99' : np.loadtxt( 'Caso1.dat' ),
#             '0.90' : np.loadtxt( 'Caso2.dat' ),
#             '0.80' : np.loadtxt( 'Caso3.dat' ),
#             '0.70' : np.loadtxt( 'Caso4.dat' ),
#             '0.60' : np.loadtxt( 'Caso5.dat' ) }




# # Plot simulation files

# for key in sorted(lbFiles.keys(), reverse = True):

#     plt.plot( lbFiles[key][:,0] / 3000., lbFiles[key][:,1] * 12., label = '$T_b = {}$'.format(key), linestyle = '-' )
#     # plt.plot( lbFiles[key][:,0] / 3000., lbFiles[key][:,1] * 12. )


# mkstyle = ['o','^','s','*','x']
    
    
# # Plot analitic results    

# for key, mk in zip(  sorted(analitica.keys(), reverse = True) , mkstyle ):


#     er = analitica[key]

    
#     # Split into phases for better plotting

#     erl, crl, erv, crv = [], [], [], []

#     for i in range( len(er[:,0]) -1 ):

#         if np.isclose(er[i,0], er[i+1,0]):

#             erl = er[:i,0]

#             erg = er[i+1:,0]

#             crl = er[:i,1]

#             crg = er[i+1:,1]        


#     erl = erl[::-200]
        
#     crl = crl[::-200]

#     erg = erg[::200]

#     crg = crg[::200]


#     plt.plot( erl * 1000,
#               crl,
#               linestyle = 'None',
#               label = '$T_b = {}$'.format(key),
#               marker = mk,
#               mfc = 'None')

#     plt.plot( erg * 1000,
#               crg,
#               linestyle = 'None',
#               marker = mk,
#               mfc = 'None')

    
    


# # Labels

# plt.ylabel(r'$\rho_r$', rotation='horizontal', labelpad=15)

# # plt.xlabel(r'$E_r \, / \, E_{r_{max}}$')
# plt.xlabel(r'$z \, / \, H$')

# # plt.legend(loc='best')        

# plt.savefig( '10.png', format='png', dpi=600 )

# # plt.show()
