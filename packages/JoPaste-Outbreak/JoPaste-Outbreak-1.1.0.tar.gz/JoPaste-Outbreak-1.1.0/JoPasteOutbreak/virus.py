class Virus:
    def __init__(self, name, long_name, r0, mortality_rate):
        self._name = name
        self._long_name = long_name
        self._r0  = r0
        self._mortality_rate = mortality_rate
    def get_name(self):
        return self._name
    def get_long_name(self):
        return self._long_name
    def get_r0(self):
        return self._r0
    def get_mortality_rate(self):
        return self._mortality_rate
