import converterUtils as cu
from BasicStuff.UnitConverter.converterUtils import to_kilograms


class Pounds:
    def __init__(self, lbs):
        self.lbs = lbs

    def get(self):
        print(self.lbs)

    def to_kg(self):
        return to_kilograms(float(self.lbs))


inpPounds = Pounds(input("Enter a Pounds: "))
inpPounds.get()
print(inpPounds.to_kg())