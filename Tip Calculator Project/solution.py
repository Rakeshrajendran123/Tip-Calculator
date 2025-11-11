#Initial welcome note printed on the screen for User
print("Welcome to the tip calculator!")

# Asking user to input the bill amount
bill = float(input("What was the total bill? $ "))

#Asking the user to input % of tip needs to added to the bill
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# Calculate tip percentage and add to bill
tip = bill +(bill*(tip/100))

#Asking the user among how many people bill needs to be split
people = int(input("How many people to split the bill? "))

#Total amount after bill splitting
people= tip/people

#Final amount to be paid among people with 2 decimal points
final_amount= round(people,2)

#Print the message on screen on how much each person should pay
print(f"The amount each person should pay is $ {final_amount} " )



