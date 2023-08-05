"""https://de.wikipedia.org/wiki/Nat%C3%BCrliche_Einheiten"""
import math
from .prefix import *
from . import massdimension as bu
import scipy.constants as const

class hep_unit(bu.massdimension_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

pi = math.pi

eV = hep_unit(massdim='energy')
speed_of_light = c = hep_unit(massdim='length')/hep_unit(massdim='time')
boltzmann_constant = k_B = hep_unit(massdim='energy')/hep_unit(massdim='temperature')
planck_constant = h_bar = hep_unit(massdim='energy')*hep_unit(massdim='time')
vacuum_permittivity = epsilon_0 = hep_unit(massdim='mass')**-1*hep_unit(massdim='length')**-3*hep_unit(massdim='time')**2


# fundamental
_c0 = const.c * c  # m/s
_h_bar0 = const.hbar/const.e*h_bar
_kb0 = const.k/const.e*k_B

# from wikipedia https://de.wikipedia.org/wiki/Nat%C3%BCrliche_Einheiten
J = joule = 1/(const.e)*eV
meter = 1/_h_bar0/_c0 * hep_unit(massdim='length')
s = second = 1/_h_bar0*hep_unit(massdim='time')
gram = 1/kilo*(1/(const.e/const.c**2)) * hep_unit(massdim='mass')
coulomb = 1/(const.epsilon_0*const.hbar*const.c)**(1/2)
ampere = coulomb/second

# *c0*c0
kelvin = 1*_kb0*hep_unit(massdim='temperature')

# composite
barn = 1e-28*meter**2
u = 1/(const.Avogadro)*gram
Bq = 1/s
Ci = 37*giga * Bq
year = const.year* s  # inclusive
Hz = hertz = 1/s
W = watt = J/s
lightyear = ly = year * c

# planck
planck_mass = 1.2e19*giga*eV
planck_length = 1/planck_mass
planck_time = planck_length
planck_temperature = planck_mass
planck_energy = planck_mass