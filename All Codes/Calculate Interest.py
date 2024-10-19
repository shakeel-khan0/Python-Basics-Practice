principle_amount = float(input("Enter principle amount: "))
irate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

interest = irate/100

rate_of_interest = (principle_amount * interest * time) / 100

print("Simple interest = " + str(rate_of_interest))