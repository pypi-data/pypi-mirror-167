import numpy as np

class IncompatibleUnitsException(Exception):
    pass

def _merge_units_add(unit_array):
    d = {}
    for u in unit_array:
        for k,v in u.items():
            if k in d:
                d[k] = d[k] + v
            else:
                d[k] = v
    # remove zero units
    for unit in list(d.keys()):
        if d[unit] == 0:
            del d[unit]
    return d

def _invert_units(units):
    return {k: -v for k,v in units.items()}

class base_unit:
    def __init__(self, val=1, units=None):
        self.value = val
        if units is None:
            units = {}
        self.units = units

    def is_number(self):
        return self.units == {} or np.all([v == 0 for k,v in self.units.items()])

    def check (self,other):
        assert self.compatible(other)

    def compatible(self, other):
        return self.units==other.units

    def to(self,unit_class):
        return unit_class.from_si(self.to_si())

    def to_si(self):
        raise NotImplementedError()

    def from_si(self):
        raise NotImplementedError()

    def __pow__(self, other, modulo=None):
        if isinstance(other, base_unit):
            assert other.is_number()
            other = other.value
        return self.__class__(self.value**other, {k:v*other for k,v in self.units.items()})

    def __rpow__(self, other, modulo=None):
        assert self.is_number()
        return other**self.value

    def __radd__(self, other):
        if isinstance(other, base_unit):
            if not self.compatible(other):
                raise IncompatibleUnitsException(str(self) + " and " + str(other) + " are not addible")
            return other.__class__(other.value+self.value, self.units)
        else:
            assert self.is_number()
            return other+self.value

    def __add__(self, other):
        if isinstance(other, base_unit):
            if not self.compatible(other):
                raise IncompatibleUnitsException(str(self) + " and " + str(other) + " are not addible")
            return self.__class__(self.value + other.value, self.units)
        else:
            assert self.is_number()
            return self.value+other

    def __rsub__(self, other):
        if isinstance(other, base_unit):
            if not self.compatible(other):
                raise IncompatibleUnitsException(str(self) + " and " + str(other) + " are not subtractable")
            return other.__class__(other.value - self.value, self.units)
        else:
            assert self.is_number()
            return other - self.value

    def __sub__(self, other):
        if isinstance(other, base_unit):
            if not self.compatible(other):
                raise IncompatibleUnitsException(str(self) + " and " + str(other) + " are not subtractable")
            return self.__class__(self.value - other.value, self.units)
        else:
            assert self.is_number()
            return self.value-other

    def __rmul__(self, other):
        if isinstance(other, base_unit):
            ret = other.__class__(other.value * self.value,_merge_units_add([self.units, other.units]))
        else:
            ret = self.__class__(other * self.value, self.units)
        if ret.is_number():
            return ret.value
        else:
            return ret

    def __mul__(self, other):
        if isinstance(other, base_unit):
            ret = self.__class__(self.value * other.value,_merge_units_add([self.units, other.units]))
        else:
            ret = self.__class__(self.value * other, self.units)
        if ret.is_number():
            return ret.value
        else:
            return ret

    def __rtruediv__(self, other):
        if isinstance(other, base_unit):
            ret = other.__class__(other.value / self.value,_merge_units_add([_invert_units(self.units), other.units]))
        else:
            ret = self.__class__(other / self.value, _invert_units(self.units))
        if ret.is_number():
            return ret.value
        else:
            return ret

    def __truediv__(self, other):
        if isinstance(other, base_unit):
            ret = self.__class__(self.value / other.value,_merge_units_add([self.units, _invert_units(other.units)]))
        else:
            ret = self.__class__(self.value / other, self.units)
        if ret.is_number():
            return ret.value
        else:
            return ret

    def __str__(self):
        if self.units== {}:
            return self.value.__str__()
        return self.value.__str__() + "[" + self.units.__str__() + "]"

    def __repr__(self):
        if self.units == {}:
            return self.value.__repr__()
        return self.value.__repr__() + "[" + self.units.__repr__() + "]"

    def __format__(self, fmt):
        if self.units== {}:
            return self.value.__format__(fmt)
        return self.value.__format__(fmt) + "[" + self.units.__repr__() + "]"