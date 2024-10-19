weight = float(input("Enter you weight: "))
unit = input("lbs & kg : ")
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"Your are {convert} kilos")
else:
    convert = weight / 0.45
    print(f"you are {convert} pounds")