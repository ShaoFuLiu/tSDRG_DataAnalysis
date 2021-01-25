# Dimerization & String Order Parameter 
### Plot
import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

spin = int(2)
BC = 'PBC'
P = 10
Ls = [16,32]
Jdis = ['Jdis200','Jdis205','Jdis210','Jdis215','Jdis220']
Dimer = ["Dim000"]
Ns = [1000]
init_seed = 1

for n in range(len(Ns)):
    N = Ns[n]
    for l in range(len(Ls)):
        L = Ls[l]
        dfstr = pd.DataFrame(columns = ['Jdis', 'O^z'])
        for d in range(len(Dimer)):
            dimer = Dimer[d]
            D = float(Dimer[d][3] + '.' + Dimer[d][4])

            myfile = '/home/liusf/test/Sorting_data/Spin'+ str(spin) +'/metadata/ZL/'+ dimer + '/Jdis-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m40_jdis-zl_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)
            plt.plot(df['Jdis'], df['ZL'], "o-", markersize = 8, label = 'L=%d, AVG(%d)' %(L, N))
            if (N != 1):
                plt.errorbar(df['Jdis'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)

plt.xlabel(r'$R$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
#plt.xlim(0.1,1.5)
plt.ylim(-0.5, 0.1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'R vs $Z(L)$, spin = %s, $\dimer$ = %s, $\chi$ = 40' % (spin, D), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( 'Spin'+ str(spin) +'_' + BC +'_'+ dimer +'_P'+ str(P) +'_m40_ZL-Jdis.pdf', format='pdf', dpi=4000)
plt.show()