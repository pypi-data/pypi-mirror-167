from . import base as bu

num = dict({'length': -1, 'mass': 1, 'time': -1,
           'temperature': 1, 'momentum': 1, 'energy': 1})
rev_num = dict([reversed(i) for i in num.items()])

class massdimension_unit(bu.base_unit):
    def __init__(self, val=1, units= None,massdim=0):
        self.value = val
        if(massdim in num):
            massdim = num[massdim]
        if units is None:
            units = {}
        self.units = units 
        if "massdimension" not in self.units.keys():
            self.units["massdimension"] = massdim
        
    def __str__(self):
        if self.units.keys() == {"massdimension"}:
            return self.value.__str__() + "[" + self.units["massdimension"].__str__() + "]"
        else:
            return super().__str__()

    def __repr__(self):
        if self.units.keys() == {"massdimension"}:
            return self.value.__repr__() + "[" + self.units["massdimension"].__repr__() + "]"
        else:
            return super().__repr__()

    def __format__(self, fmt):
        if self.units.keys() == {"massdimension"}:
            return self.value.__format__(fmt) + "[" + self.units["massdimension"].__repr__() + "]"
        else:
            return super().__format__(fmt)