# Check whether the number entered by user is Odd or Even


#Print welcome message to Odd or even game
print("Welcome to Odd or Even game ")

#Ask user to input the number to check if it odd or even
x= int(input("Enter the number: "))

#Apply if else to check whether the number is Odd or Even
if x % 2 == 0:
    print(f"The entered number {x} is Even ")
else:
    print(f"The entered number {x} is Odd ")

