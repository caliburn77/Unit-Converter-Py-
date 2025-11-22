import converterUtils as cu
import time

#takes pounds and converts to kg
def case_1():
    inpPounds = float(input("Enter Pounds: "))
    print(f'{inpPounds}lbs = {cu.to_kilograms(inpPounds)}kg.')
    time.sleep(3)

#takes kg and converts to pounds
def case_2():
    inpKilograms = float(input("Enter Kilograms: "))
    print(f'{inpKilograms}kg = {cu.to_pounds(inpKilograms)}lbs.')
    time.sleep(3)

#takes inches and converts to centimeters
def case_3():
    inpInches = float(input("Enter Inches: "))
    print(f'{inpInches}in = {cu.to_centimeters(inpInches)}cm.')
    time.sleep(3)

#takes centimeters and converts inches
def case_4():
    inpCentimeters = float(input("Enter Centimeters: "))
    print(f'{inpCentimeters}cm = {cu.to_inches(inpCentimeters)}in.')
    time.sleep(3)

#takes mph and converts to kph
def case_5():
    inpMiles = float(input("Enter the speed in Miles per Hour: "))
    print(f'{inpMiles}mph = {cu.to_kph(inpMiles)}kph.')
    time.sleep(3)

#takes kph and converts to mph
def case_6():
    inpKm = float(input("Enter the speed in Kilometers per Hour: "))
    print(f'{inpKm}km = {cu.to_mph(inpKm)}mph.')
    time.sleep(3)

#takes <feet>' <inches>" and converts to inches
def case_7():
    inpFeet = float(input("Enter Feet: "))
    inpInches = float(input("Enter Inches: "))
    print(f'{inpFeet}\' {inpInches}\" = {cu.feetinches_to_inches(inpFeet, inpInches)}in.')
    time.sleep(3)

#takes inches and converts to <feet>' <inches>"
def case_8():
    inches = float(input("Enter Inches: "))
    resFeet, resInches = cu.inches_to_feetinches(inches)
    print(f'{inches}in = {resFeet}\' {resInches}\".')
    time.sleep(3)

#default case
def case_default():
    print("Please enter a valid number.")
    time.sleep(3)

#test