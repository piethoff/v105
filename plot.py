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

x, y = np.genfromtxt('content/messwerte_schwing.txt', unpack=True)

plt.xlabel(r'$B^{-1}/\si[per-mode=reciprocal]{\per\tesla}$')
plt.ylabel(r'$T^2/\si{\second\squared}$')
plt.grid(True, which='both')


# Fitvorschrift
def f(x, A, B):
    return A*x + B      #jeweilige Fitfunktion auswaehlen:

params, covar = curve_fit(f, x, y)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('A') + i), "=" , uparams[i])
print()

plt.plot(x, f(x, *params), "xkcd:orange", label=r'Regression' )
plt.plot(x, y, ".", color="xkcd:blue", label="Messwerte")



plt.tight_layout()
plt.legend()
plt.savefig('build/schwing.pdf')
plt.clf()

x, y = np.genfromtxt('content/messwerte_praez.txt', unpack=True)

plt.xlabel(r'$B/\si{\tesla}$')
plt.ylabel(r'$T^{-1}/\si[per-mode=reciprocal]{\per\second}$')
plt.grid(True, which='both')


# Fitvorschrift
def f(x, A, B):
    return A*x + B      #jeweilige Fitfunktion auswaehlen:

params, covar = curve_fit(f, x, y)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('A') + i), "=" , uparams[i])
print()

plt.plot(x, f(x, *params), "xkcd:orange", label=r'Regression' )
plt.plot(x, y, ".", color="xkcd:blue", label="Messwerte")



plt.tight_layout()
plt.legend()
plt.savefig('build/praez.pdf')
plt.clf()

x, y = np.genfromtxt('content/messwerte_grav.txt', unpack=True)

x /=100
y *= 0.00136
plt.xlabel(r'$r/\si[per-mode=reciprocal]{\meter}$')
plt.ylabel(r'$B/\si{\tesla}$')
plt.grid(True, which='both')


# Fitvorschrift
def f(x, A, B):
    return A*x + B      #jeweilige Fitfunktion auswaehlen:

params, covar = curve_fit(f, x, y)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('A') + i), "=" , uparams[i])
print()

plt.plot(x, f(x, *params), "xkcd:orange", label=r'Regression' )
plt.plot(x, y, ".", color="xkcd:blue", label="Messwerte")



plt.tight_layout()
plt.legend()
plt.savefig('build/grav.pdf')
plt.clf()
