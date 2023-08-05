"""https://en.wikipedia.org/wiki/Natural_units"""
import math
import scipy.constants as const

from natural_units.core import ot, to
from .prefix import kilo
from . import base as bu
from . import si
pi = math.pi

class stoney_unit(bu.base_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

    def from_si(self):
        siv = stoney_unit(1,{})*self
        map = {'coulomb':coulomb/si.coulomb,'metre':meter/si.meter,'kilogram':kilogram/si.kilogram,'second':second/si.second}
        for u in self.units:
            siv *= ot(map[u]**self.units[u])
        return siv

    def to_si(self):
        siv = si.si_unit(1,{})*self
        map = {'charge':coulomb/si.coulomb,'length':meter/si.meter,'mass':kilogram/si.kilogram,'time':second/si.second}
        for u in self.units:
            siv *= to(map[u]**self.units[u])
        return siv

speed_of_light = c = stoney_unit(1,{'length':1,'time':-1})
gravitational_constant = G = stoney_unit(1,{'mass':-1,'length':3,'time':-2})
coulomb_constant = k_e = stoney_unit(1,{'mass':-1,'length':-3,'time':2,'charge':2})
electron_charge = e = stoney_unit(1,{'charge':1})

# measured
proton_to_electron_mass_ratio = const.proton_mass/const.electron_mass
fine_structure_constant = alpha = const.fine_structure
gravitational_coupling_constant = alpha_G = const.G*const.m_e**2/const.hbar/const.c

# derived
vacuum_permittivity = epsilon_0 = 1/(4*pi*k_e)
reduced_planck_constant= h_bar = (e**2/(4*pi*epsilon_0*c*alpha))
electron_mass = m_e = (h_bar*c*gravitational_coupling_constant/G)**(1/2)
proton_mass = m_p = proton_to_electron_mass_ratio*m_e

# undefined
boltzmann_constant = k_B = None

# si conversion
meter = metre = 1/(const.G *const.e**2/(4*pi*const.epsilon_0*const.c**4))**(1/2) * stoney_unit(1,{'length':1})
gram = 1/kilo * 1/(const.e**2/(4*pi*const.epsilon_0*const.G))**(1/2)  * stoney_unit(1,{'mass':1})
kilogram = kilo*gram
second = 1/(const.G*const.e**2/(4*pi*const.epsilon_0*const.c**6))**(1/2) * stoney_unit(1,{'time':1})
coulomb = 1/(const.e) * stoney_unit(1,{'charge':1})
ampere = coulomb/second