cost = int(input("Enter total cost of meal: "))
tip = float(input("Enter %age of tip: "))

percentage = tip/100 * cost
total_amount = percentage + cost

print("Total cost of meal including tip = " + str(total_amount))
