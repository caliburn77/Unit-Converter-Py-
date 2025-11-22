import caseUtils as cu

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
                    0. Exit Application
    ''')

    match choice:
        case "1":
            cu.case_1()
        case "2":
            cu.case_2()
        case "3":
            cu.case_3()
        case "4":
            cu.case_4()
        case "5":
            cu.case_5()
        case "6":
            cu.case_6()
        case "7":
            cu.case_7()
        case "8":
            cu.case_8()
        case "9":
            cu.case_9()
        case "0":
            break
        case _:
            cu.case_default()
