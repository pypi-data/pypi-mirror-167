"""https://en.wikipedia.org/wiki/Planck_units"""

import math
import scipy.constants as const

from natural_units.core import ot, to
from .prefix import kilo
from . import base as bu
from . import si
pi = math.pi

class planck_unit(bu.base_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

    def from_si(self):
        siv = planck_unit(1,{})*self
        map = {'kelvin':kelvin/si.kelvin,'metre':meter/si.meter,'kilogram':kilogram/si.kilogram,'second':second/si.second}
        for u in self.units:
            siv *= ot(map[u]**self.units[u])
        return siv

    def to_si(self):
        siv = si.si_unit(1,{})*self
        map = {'temperature':kelvin/si.kelvin,'length':meter/si.meter,'mass':kilogram/si.kilogram,'time':second/si.second}
        for u in self.units:
            siv *= to(map[u]**self.units[u])
        return siv


speed_of_light = c = planck_unit(1,{'length':1,'time':-1})
reduced_planck_constant= h_bar = planck_unit(1,{'mass':1,'length':2,'time':-1})
planck_constant = h = 2*pi*h_bar
gravitational_constant = G = planck_unit(1,{'mass':-1,'length':3,'time':-2})
boltzmann_constant = k_B = planck_unit(1,{'mass':1,'length':2,'time':-2,'temperature':-1})

# measured
gravitational_coupling_constant = alpha_G = const.G*const.m_e**2/const.hbar/const.c
proton_to_electron_mass_ratio = const.proton_mass/const.electron_mass


mass_eletron = m_e = (h_bar*c*gravitational_coupling_constant/G)**(1/2)
mass_proton = m_p = proton_to_electron_mass_ratio*m_e

# undefined
fine_structure_constant = alpha = None
elementary_charge = e = None
vacuum_permittivity = epsilon_0 = None
coulomb_constant = k_e = None

# si conversion
meter = metre = 1/(const.hbar*const.G/(const.c**3))**0.5 * planck_unit(1,{'length':1})
gram = 1/kilo * 1/(const.hbar * const.c/const.G)**0.5 * planck_unit(1,{'mass':1})
kilogram = kilo*gram
second = 1/(const.hbar*const.G/(const.c**5))**0.5 * planck_unit(1,{'time':1})
kelvin = 1/(const.hbar*const.c**5/(const.G * const.k**2))**0.5 * planck_unit(1,{'temperature':1})
