import math

class Stiffness:
    def __init__(self, data):
        self.data = data
        self.g = 9.807

    def maximal_force(self):
        fm = self.data['MASS'] * self.g * (math.pi / 2) * ((self.data['TIME_FLIGHT'] / self.data['TIME_CONTACT']) + 1)
        return fm * 0.001

    def delta_cm(self):
        return ((self.maximal_force() * math.pow(self.data['TIME_CONTACT'], 2)) / (self.data['MASS'] * math.pow(math.pi, 2))) + self.g * (math.pow(self.data['TIME_CONTACT'], 2) / 8)

    def vertical_stiffness(self):
        return self.maximal_force() * math.pow(self.delta_cm(), -1)

    def delta_l(self):
        return self.data['LENGTH_LEG'] - math.sqrt(math.pow(self.data['LENGTH_LEG'], 2) - math.pow((self.data['SPEED'] * self.data['TIME_CONTACT']) / 2, 2)) + self.delta_cm()

    def leg_stiffness(self):
        return self.maximal_force() * math.pow(self.delta_l(), -1)

    def results(self):
        return {
            'LEG_STIFFNESS': self.leg_stiffness().values[0],
            'VERTICAL_STIFFNESS': self.vertical_stiffness().values[0],
            'MAXIMAL_FORCE': self.maximal_force().values[0],
            'DELTA_CM': self.delta_cm().values[0],
            'DELTA_LENGTH': self.delta_l().values[0]
        }






