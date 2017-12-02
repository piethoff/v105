import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
import scipy.constants.constants as const
from uncertainties import ufloat
from uncertainties import unumpy


mpl.use('pgf')
mpl.rcParams.update({
    'pgf.preamble': r'\usepackage{siunitx}',
})

x, y = np.genfromtxt('content/Messwerte_schwing.txt', unpack=True)

plt.plot(x, y, 'rx')
plt.xlabel(r'$1/B[\si{1\per\tesla}]$')
plt.ylabel(r'$T^2[\si{\second\squared}]$')
plt.grid(True, which='both')


# Fitvorschrift
def f(x, A, B):
    return A*x + B      #jeweilige Fitfunktion auswaehlen:

params, covar = curve_fit(f, x, y)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('A') + i), "=" , uparams[i])
print()

plt.plot(x, f(x, *params), "b--", label=r'Regression' )



plt.tight_layout()
plt.savefig('schwing.pdf')
plt.clf()
