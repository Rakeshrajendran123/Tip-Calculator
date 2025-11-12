#Print welcome message on the screen
print(" Welcome to rollercoaster ride ")

#Ask the user to input the height
height= int(input(" Enter your height: "))

# Use if/elif/else condition to check for height and then check for age in multiple brackets
if height >= 120:
    print(" You are eligible to ride ")
    age = int(input(" Enter your age: "))
    if age >=5 and age <= 12:
        print(" You need to pay Rs 5")
    elif age > 12 and age <= 18:
        print(" You need to pay Rs 10 ")
    else:
        print(" You need to pay Rs 15 ")
        print(" Enjoy the Ride ")
else:
    print(" You need to be above 120 cm to avail this ride ")

