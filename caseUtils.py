import converterUtils as cu
import time

#takes pounds and converts to kg
def case_1():
    while True:
        inpPounds = input("Enter Pounds: ")
        match inpPounds:
            case str(s):
                try:
                    float_value=float(s)
                    print(f'{s}lbs = {cu.to_kilograms(float_value)}kg.')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print("Please enter a valid float as a string. ")

#takes kg and converts to pounds
def case_2():
    while True:
        inpKilograms = input("Enter Kilograms: ")
        match inpKilograms:
            case str(s):
                try:
                    float_value=float(s)
                    print(f'{s}kg = {cu.to_pounds(float_value)}lbs.')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')

#takes inches and converts to centimeters
def case_3():
    while True:
        inpInches = input("Enter Inches: ")
        match inpInches:
            case str(s):
                try:
                    float_value=float(s)
                    print(f'{s}in = {cu.to_centimeters(float_value)}cm. ')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')

#takes centimeters and converts inches
def case_4():
    while True:
        inpCentimeters = input("Enter Centimeters: ")
        match inpCentimeters:
            case str(s):
                try:
                    float_value=float(s)
                    print(f'{s}cm = {cu.to_inches(float_value)}in. ')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')

#takes mph and converts to kph
def case_5():
    while True:
        inpMiles = input("Enter the speed in Miles per Hour: ")
        match inpMiles:
            case str(s):
                try:
                    float_value=float(s)
                    print(f'{s}mph = {cu.to_kph(float_value)}kph.')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')

#takes kph and converts to mph
def case_6():
    while True:
        inpKm = input("Enter the speed in Kilometers per Hour: ")
        match inpKm:
            case str(s):
                try:
                    float_value=float(s)
                    print(f'{s}kph = {cu.to_mph(float_value)}mph. ')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')

#takes <feet>' <inches>" and converts to inches
def case_7():
    while True:
        inpFeet = input("Enter Feet: ")
        match inpFeet:
            case str(s):
                try:
                    feet_float=float(s)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')
    while True:
        inpInches = input("Enter Inches: ")
        match inpInches:
            case str(s):
                try:
                    inches_float=float(s)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')
    print(f'{feet_float}\' {inches_float}\" = {cu.feetinches_to_inches(feet_float, inches_float)}in. ')
    time.sleep(3)

#takes inches and converts to <feet>' <inches>"
def case_8():
    while True:
        inches = input("Enter Inches: ")
        match inches:
            case str(s):
                try:
                    inches_float=float(s)
                    res_feet, res_inches=cu.inches_to_feetinches(inches_float)
                    print(f'{inches_float}in = {res_feet}\' {res_inches}\". ')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')

#takes feet and converts to meters
def case_9():
    while True:
        feet = input("Enter Feet: ")
        match feet:
            case str(s):
                try:
                    feet_float=float(s)
                    print(f'{s}ft = {cu.feet_to_meters(feet_float)}m. ')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')

#takes meters and converts to feet
def case_10():
    while True:
        meters = input("Enter Meters: ")
        match meters:
            case str(s):
                try:
                    meters_float=float(s)
                    print(f'{s}m = {cu.meters_to_feet(meters_float)}ft. ')
                    time.sleep(3)
                    break
                except ValueError:
                    print('Please enter a valid float. ')
            case _:
                print('Please enter a valid float as a string. ')
#default case
def case_default():
    print("Please enter a valid number from the list.")
    time.sleep(3)