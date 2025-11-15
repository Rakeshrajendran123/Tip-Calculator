#print on the screen welcome message
print("Welcome to the rollercoaster ride")
height= int(input("Enter you height ? "))
bill =0
if height >= 120 :
     print("You can go ahead and ride")
     age= int(input("Enter your age ? "))
     if age <=12:
         print("It will cost $5")
         bill=5
     elif age > 12 and age <=18:
         print("It will cost $7")
         bill=7
     elif age >=45 and age <=55:
         print("You are free to ride")
         bill=0
     else:
         print("It will cost $12")
         bill=12
#Ask user if they want photo to be taken add $3 to their overall bill
     photo= input("Do you want photos ? for Yes type Y and for No type N: ")
     if photo == "Y":
         if age >=45 and age <=55:
          bill=0
         else:
             bill+=3
     print(f"Your final bill is ${bill}")
else:
    print("You can't ride because you need to grow up bit")