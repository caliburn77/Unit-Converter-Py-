from classesUtils import *
import time

#takes pounds and converts to kg
def case_1():
    while True:
        inpPounds = Pounds(input("Enter Pounds: "))
        if type(inpPounds.get_as_float()) == float:
            break
    print(f'{inpPounds.get_as_float()}lbs = {inpPounds.to_kg()}kg. ')
    time.sleep(3)

#takes kg and converts to pounds
def case_2():
    while True:
        inpKilograms = Kilograms(input("Enter Kilograms: "))
        if type(inpKilograms.get_as_float()) == float:
            break
    print(f'{inpKilograms.get_as_float()}kg = {inpKilograms.to_lbs()}lbs. ')
    time.sleep(3)

#takes inches and converts to centimeters
def case_3():
    while True:
        inpInches = Inches(input("Enter Inches: "))
        if type(inpInches.get_as_float()) == float:
            break
    print(f'{inpInches.get_as_float()}in = {inpInches.to_cm()}cm. ')
    time.sleep(3)

#takes centimeters and converts inches
def case_4():
    while True:
        inpCentimeters = Centimeters(input("Enter Centimeters: "))
        if type(inpCentimeters.get_as_float()) == float:
            break
    print(f'{inpCentimeters.get_as_float()}cm = {inpCentimeters.to_in()}in. ')
    time.sleep(3)

#takes mph and converts to kph
def case_5():
    while True:
        inpMiles = MPH(input("Enter the speed in Miles Per Hour: "))
        if type(inpMiles.get_as_float()) == float:
            break
    print(f'{inpMiles.get_as_float()}mph = {inpMiles.to_kph()}kph. ')
    time.sleep(3)

#takes kph and converts to mph
def case_6():
    while True:
        inpKm = KPH(input("Enter the speed in Kilometers Per Hour: "))
        if type(inpKm.get_as_float()) == float:
            break
    print(f'{inpKm.get_as_float()}kmh = {inpKm.to_mph()}mph. ')
    time.sleep(3)

#takes <feet>' <inches>" and converts to inches
def case_7():
    while True:
        inpFeet = Feet(input("Enter Feet: "))
        if type(inpFeet.get_as_float()) == float:
            break
    while True:
        inpInches = Inches(input("Enter Inches: "))
        if type(inpInches.get_as_float()) == float:
            break
    print(f'{inpFeet.get_as_float()}\' {inpInches.get_as_float()}\" = {inpFeet.feetin_to_in(inpInches.get_as_float())}in. ')
    time.sleep(3)

#takes inches and converts to <feet>' <inches>"
def case_8():
    while True:
        inpInches = Inches(input("Enter Inches: "))
        if type(inpInches.get_as_float()) == float:
            break
    resFeet, resInches = inpInches.in_to_feetin()
    print(f'{inpInches.get_as_float()}in = {resFeet}\' {resInches}\". ')
    time.sleep(3)

#takes feet and converts to meters
def case_9():
    while True:
        inpFeet = Feet(input("Enter Feet: "))
        if type(inpFeet.get_as_float()) == float:
            break
    print(f'{inpFeet.get_as_float()}ft = {inpFeet.feet_to_m()}m. ')
    time.sleep(3)

#takes meters and converts to feet
def case_10():
    while True:
        meters = Meters(input("Enter Meters: "))
        if type(meters.get_as_float()) == float:
            break
    print(f'{meters.get_as_float()}m = {meters.meters_to_ft()}ft. ')
    time.sleep(3)

def case_11():
    while True:
        grams = Grams(input("Enter Grams: "))
        if type(grams.get_as_float()) == float:
            break
    print(f'{grams.get_as_float()}g = {grams.to_oz()}oz. ')
    time.sleep(3)

def case_12():
    while True:
        ounces = Ounces(input("Enter Ounces: "))
        if type(ounces.get_as_float()) == float:
            break
    print(f'{ounces.get_as_float()}oz = {ounces.to_grams()}g. ')
    time.sleep(3)

#default case
def case_default():
    print("Please enter a valid number from the list.")
    time.sleep(3)