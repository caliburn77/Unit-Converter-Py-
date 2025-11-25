import caseUtils as caseu

while True:
    choice = input('''Enter the number corresponding to which unit(s) you would like to convert: 
                    1. Pounds -> Kilograms
                    2. Kilograms -> Pounds
                    3. Inches -> Centimeters
                    4. Centimeters -> Inches
                    5. Miles per Hour -> Kilometers per Hour
                    6. Kilometers per Hour -> Miles per Hour
                    7. <Feet>' <Inches>" -> Inches
                    8. Inches -> <Feet>' <Inches>"
                    9. Feet -> Meters
                    10. Meters -> Feet
                    11. Grams -> Ounces
                    12. Ounces -> Grams
                    0. Exit Application
    ''')

    match choice:
        case "1":
            caseu.case_1()
        case "2":
            caseu.case_2()
        case "3":
            caseu.case_3()
        case "4":
            caseu.case_4()
        case "5":
            caseu.case_5()
        case "6":
            caseu.case_6()
        case "7":
            caseu.case_7()
        case "8":
            caseu.case_8()
        case "9":
            caseu.case_9()
        case "10":
            caseu.case_10()
        case "11":
            caseu.case_11()
        case "12":
            caseu.case_12()
        case "0":
            break
        case _:
            caseu.case_default()
