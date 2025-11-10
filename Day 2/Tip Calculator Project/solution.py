print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ "))

tip = int(input("What percentage tip would you like to give? 10 12 15 "))
tip = bill +(bill*(tip/100))


people = int(input("How many people to split the bill? "))
people= tip/people
print(round(people,2))



