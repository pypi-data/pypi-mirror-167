"""https://en.wikipedia.org/wiki/Geometrized_unit_system"""
import math
from .prefix import *
from . import base as bu
from natural_units import prefix


class geometrized_unit(bu.base_unit):
    def __init__(self, val=1, units= None,lengthdim=0):
        self.value = val
#        if(lengthdim in num):
#            lengthdim = num[lengthdim]
        if units is None:
            units = {}
        self.units = units 
        if "lengthdimension" not in self.units.keys():
            print("set",self.units)
            self.units["lengthdimension"] = lengthdim
        
    def __str__(self):
        if self.units.keys() == {"lengthdimension"}:
            return self.value.__str__() + "[" + self.units["lengthdimension"].__str__() + "]"
        else:
            return super().__str__()

    def __repr__(self):
        if self.units.keys() == {"lengthdimension"}:
            return self.value.__repr__() + "[" + self.units["lengthdimension"].__repr__() + "]"
        else:
            return super().__repr__()

    def __format__(self, fmt):
        if self.units.keys() == {"lengthdimension"}:
            return self.value.__format__(fmt) + "[" + self.units["lengthdimension"].__repr__() + "]"
        else:
            return super().__format__(fmt)

c = geometrized_unit(lengthdim=0)
G = geometrized_unit(lengthdim=0)


# fundamental
c0 = 299792458 * c *100  # cm/s
G0 = 6.6741e-8 # cm^3/g/s^2

cm = geometrized_unit(lengthdim=1)
meter = cm/prefix.centi

g = gram = G0/c0**2*geometrized_unit(lengthdim=1)
s = second = c0*geometrized_unit(lengthdim=1)
erg = g*cm**2*s**-2

M0 = 1.4765734*kilo*meter

