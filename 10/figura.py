import os

import postLBRun as post

import matplotlib.pyplot as plt

import numpy as np





# van Der Waals properties

Er_max = 1e-03

b = 4.0

plt.style.use('../custom.mplstyle')


# Load data files

lbFiles = { '0.99' : np.loadtxt( 'Caso1.dat' ),
            '0.90' : np.loadtxt( 'Caso2.dat' ),
            '0.80' : np.loadtxt( 'Caso3.dat' ),
            '0.70' : np.loadtxt( 'Caso4.dat' ),
            '0.60' : np.loadtxt( 'Caso5.dat' ) }

analitica = { '0.99' : np.loadtxt( 'Tr_0.990_0.990_cbar_1.000.dat' ),
              '0.90' : np.loadtxt( 'Tr_0.990_0.900_cbar_1.000.dat' ),
              '0.80' : np.loadtxt( 'Tr_0.990_0.800_cbar_1.000.dat' ),
              '0.70' : np.loadtxt( 'Tr_0.990_0.700_cbar_1.000.dat' ),
              '0.60' : np.loadtxt( 'Tr_0.990_0.600_cbar_1.000.dat' ) }



# Plot simulation files

for key in sorted(lbFiles.keys(), reverse = True):

    plt.plot( lbFiles[key][:,0] / 3000., lbFiles[key][:,1] * 12., label = '$T_b = {}$'.format(key), linestyle = '-' )
    # plt.plot( lbFiles[key][:,0] / 3000., lbFiles[key][:,1] * 12. )


mkstyle = ['o','^','s','*','x']
    
    
# Plot analitic results    

for key, mk in zip(  sorted(analitica.keys(), reverse = True) , mkstyle ):


    er = analitica[key]

    
    # Split into phases for better plotting

    erl, crl, erv, crv = [], [], [], []

    for i in range( len(er[:,0]) -1 ):

        if np.isclose(er[i,0], er[i+1,0]):

            erl = er[:i,0]

            erg = er[i+1:,0]

            crl = er[:i,1]

            crg = er[i+1:,1]        


    erl = erl[::-200]
        
    crl = crl[::-200]

    erg = erg[::200]

    crg = crg[::200]


    plt.plot( erl * 1000,
              crl,
              linestyle = 'None',
              label = '$T_b = {}$'.format(key),
              marker = mk,
              mfc = 'None')

    plt.plot( erg * 1000,
              crg,
              linestyle = 'None',
              marker = mk,
              mfc = 'None')

    
    


# Labels

plt.ylabel(r'$\rho_r$')

# plt.xlabel(r'$E_r \, / \, E_{r_{max}}$')
plt.xlabel(r'$z \, / \, H$')

# plt.legend(loc='best')        

plt.savefig( '10.png', format='png', dpi=600 )

# plt.show()
