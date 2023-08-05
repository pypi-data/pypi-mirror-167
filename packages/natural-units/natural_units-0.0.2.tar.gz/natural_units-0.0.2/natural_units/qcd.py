"""https://en.wikipedia.org/wiki/Hartree_atomic_units"""
import math
from turtle import speed
import scipy.constants as const

from natural_units.core import ot, to
from .prefix import kilo
from . import base as bu
from . import si
pi = math.pi

class qcd_unit(bu.base_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

    def from_si(self):
        siv = qcd_unit(1,{})*self
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

mass_proton = m_p = qcd_unit(1,{'mass':1})
speed_of_light = c = qcd_unit(1,{'length':1,'time':-1})
reduced_planck_constant= h_bar = qcd_unit(1,{'mass':1,'length':2,'time':-1})
planck_constant = h = 2*pi*h_bar
vacuum_permittivity = epsilon_0 = qcd_unit(1,{'mass':-1,'length':-3,'time':2,'charge':2}) 

# measured
proton_to_electron_mass_ratio = const.proton_mass/const.electron_mass
fine_structure_constant = alpha = const.fine_structure
gravitational_coupling_constant = alpha_G = const.G*const.m_e**2/const.hbar/const.c

# derived
elementary_charge = e = (4*pi*alpha* epsilon_0 * h_bar * c) **(1/2)
coloumb_constant = k_e = 1/(4*pi*epsilon_0)
electron_mass = m_e = m_p/proton_to_electron_mass_ratio
gravitational_constant = G = alpha_G * h_bar*c /m_e**2


# undefined
boltzmann_constant = k_B = None

# si conversion
meter = metre = 1/(const.hbar/(const.m_p*const.c)) * qcd_unit(1,{'length':1})
gram = 1/kilo * 1/const.m_p * qcd_unit(1,{'mass':1})
kilogram = kilo*gram
second = 1/(const.hbar/const.m_p/const.c**2) * qcd_unit(1,{'time':1})
coulomb = 1/(const.e/(4*pi*const.fine_structure)) * qcd_unit(1,{'charge':1})
ampere = coulomb/second
