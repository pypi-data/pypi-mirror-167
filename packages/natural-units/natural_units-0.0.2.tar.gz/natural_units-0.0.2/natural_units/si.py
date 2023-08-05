"""https://en.wikipedia.org/wiki/International_System_of_Units"""
from . import base as bu
import math
from .prefix import kilo
import scipy.constants as const



class si_unit(bu.base_unit):
    def to_si(self):
        return self

    def from_si(other):
        return other

    def _si_units_to_str(self):
        """Convert a dictionary of SI units to a string."""
        ret = ""
        for unit, power in self.units.items():
             unit = {"metre":"m","kilogram":"kg","second":"s","ampere":"A","kelvin":"K","mole":"mol","candela":"cd"}[unit]
             if power == 1:
                 ret += unit
             else:
                 ret += unit + "^" + power.__str__()
        return ret

    def _in_si_units(self):
        """Check if a dictionary of units is in SI units."""
        return all([unit in ["metre","kilogram","second","ampere","kelvin","mole","candela"] for unit in self.units.keys()])

    def __str__(self):
        if self._in_si_units():
            return self.value.__str__() + " " + self._si_units_to_str() + ""
        else:
            return super().__str__()

    def __repr__(self):
        if self._in_si_units():
            return self.value.__repr__() + " " + self._si_units_to_str() + ""
        else:
            return super().__repr__()

    def __format__(self, fmt):
        if self._in_si_units():
            return self.value.__format__(fmt) + " " + self._si_units_to_str() + ""
        else:
            return super().__format__(fmt)

# base units
meter = metre = si_unit(1, {'metre': 1})
second = si_unit(1, {'second': 1})
kilogram = kg = si_unit(1, {'kilogram': 1})
ampere = si_unit(1, {'ampere': 1})
kelvin = si_unit(1, {'kelvin': 1})
mol = mole = si_unit(1, {'mole': 1})
candela = si_unit(1, {'candela': 1})


# derived units
gram = g = kilogram/kilo
hertz = Hz = 1 / second
joule = J = kg * meter ** 2 / second ** 2
watt = W = joule / second
volt = V = watt / ampere
coulomb = C = ampere * second


# defining constants
delta_nu_cs = 9192631770 / second
c = speed_of_light = const.c * meter / second
h = planck = const.h * joule * second
h_bar = h/(2*math.pi)
eV = electron_volt = const.e * joule
k_B = boltzmann_constant = const.k * joule / kelvin
N_A = avogadro = const.Avogadro / mole
K_cd 		= 683 *  candela / watt 
