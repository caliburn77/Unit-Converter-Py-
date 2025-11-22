from math import floor

def to_kilograms(pounds):
    return round(pounds * 0.453592, 2)

def to_pounds(kg):
    return round(kg * 2.205, 2)

def to_centimeters(inches):
    return round(inches * 2.54, 2)

def to_inches(centimeters):
    return round(centimeters / 2.54, 2)

def to_kph(mph):
    return round(mph * 1.609, 2)

def to_mph(kph):
    return round(kph / 1.609, 2)

def feetinches_to_inches(feet, inches):
    return (feet * 12) + inches

def inches_to_feetinches(inches):
    feet = floor(inches / 12)
    remain_inches = inches - (feet * 12)
    return feet, round(remain_inches, 2)

def feet_to_meters(feet):
    return round(feet / 3.281, 2)

def meters_to_feet(meters):
    return round(meters * 3.281, 2)