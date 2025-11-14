# Print welcome message on the screen
print("Welcome to Pizza Drop shop ")
pizza_size=input("What pizza size do you want? S for Small, M for Medium and L for large : ")
pepperoni=input("Do you want Pepperoni for medium or large Pizza(Y or N)? : ")
cheese = input("Do you want to add extra cheese(Y or N )?: ")

pizza_cost=0

#Pizza cost based on size

if pizza_size=="S":
    pizza_cost += 15
elif pizza_size =="M":
    pizza_cost +=20
elif pizza_size == "L":
    pizza_cost += 25
else:
    print("You have invalid size")

#Add pepperoni cost to pizza cost
if pepperoni=="Y":
     if pizza_size=="S":
         pizza_cost +=2
     else:
         pizza_cost +=3

#Add Chesse Cost to pizza cost
if cheese=="Y":
        pizza_cost +=1

# Print total cost of Pizza based on choices user made
print(f"The final bill is ${pizza_cost}")
