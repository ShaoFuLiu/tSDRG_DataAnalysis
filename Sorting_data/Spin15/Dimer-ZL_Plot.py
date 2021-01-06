# Dimerization & String Order Parameter 
### Plot
import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

spin = 1.5
BC = 'PBC'
P = 10
Ls = [64]
Jdis = ['Jdis000']

init_D = 5 #0.05
final_D = 100 #1.0
space = 5
file_num = int ((final_D - init_D)/space+1)
Dimer = ['Dim000']
for i in range(file_num):
    D = init_D + space*i
    if (D < 10):
        d = '00' + str(D)[0]
        Dimer.append('Dim' + d)
    elif (D >= 10 and D < 100):
        d = '0' + str(D)[0] + str(D)[1]
        Dimer.append('Dim' + d)
    elif (D >= 100):
        d = str(D)[0] + str(D)[1] + str(D)[2]
        Dimer.append('Dim' + d)

N = 1
chis = [30,40]
init_seed = 1

for i in range(len(Ls)):
    L = Ls[i]
    if (L == 128):
        chis = [60]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    for m in range(len(chis)):
        M = chis[m]
        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5])

            myfile = '/home/liusf/test/Sorting_data/Spin15/metadata/ZL/'+ jdis + '/Dimer-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m'+str(M)+'_dim-zl_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)
            plt.plot(df['Dimerization'], df['ZL'], "o-", markersize = 8, label = 'L=%d, $\chi$= %d' %(L, M))

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
#plt.xlim(0.1,1.5)
plt.ylim(-1, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $Z(L)$, spin = %s, $\delta$ = %s' % (spin, J), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.grid(color='b', linestyle='-', linewidth=1)
plt.savefig( 'Spin15_' + BC + '_' + jdis + '_P'+ str(P) +'_ZL-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()