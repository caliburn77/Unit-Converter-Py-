import converterUtils as cu

class Unit:
    def __init__(self, entry):
        self.entry = entry

    def get_as_float(self):
        try:
            return float(self.entry)
        except ValueError:
            print("Please enter a valid float. ")


class Pounds(Unit):
    def to_kg(self):
        return cu.to_kilograms(self.get_as_float())


class Kilograms(Unit):
    def to_lbs(self):
        return cu.to_pounds(self.get_as_float())


class Inches(Unit):
    def to_cm(self):
        return cu.to_centimeters(self.get_as_float())

    def in_to_feetin(self):
        return cu.inches_to_feetinches(self.get_as_float())


class Feet(Unit):
    def feetin_to_in(self, inches):
        return cu.feetinches_to_inches(self.get_as_float(), inches)

    def feet_to_m(self):
        return cu.feet_to_meters(self.get_as_float())


class Centimeters(Unit):
    def to_in(self):
        return cu.to_inches(self.get_as_float())


class Meters(Unit):
    def meters_to_ft(self):
        return cu.meters_to_feet(self.get_as_float())


class MPH(Unit):
    def to_kph(self):
        return cu.to_kph(self.get_as_float())


class KPH(Unit):
    def to_mph(self):
        return cu.to_mph(self.get_as_float())