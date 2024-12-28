#a=int(input("Enter the age ->"))
a=0
while a == 0 :
    a=int(input("Enter the age ->"))
if a < 99 and a>18:
    print("you are eligible to vote")
elif a > 13 and a < 18 :
    print("you are not eligible to vote")
elif a < 13 :
    print("you are chlid ") 
else :
    print("   Welcome to Hevan ")