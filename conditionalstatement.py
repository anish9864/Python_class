#Conditional statement -> logic checking

#if statement
# else of statement {elif}
#else statement

# if statement requires identation in end {:}

# age = int(input("Your age is "))

# if age >=18 :
#     print("You can vote.")
    
# else:
#     print("You can't vote.")
   
    
    
# num = int(input("Enter the number "))

# if num % 2 == 0:
#     print(f"{num} is even Number.")
    
# else :
#     print(f"{num} is odd Number")
    
    
    
#Nested if else conditions

# num = int(input("Enter the number "))

# if num>= 0:
#     if num % 2 == 0:
#         print(f"{num} is even Number.")
    
#     else :
#         print(f"{num} is odd number")
    
    
   
# else :
#     print(f"{num} is negative number")

    
marks = int(input("Marks "))

if marks >= 80:
    print("A Grade")
elif marks>= 70:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 40:
    print("D Grade")
else:
    print("Fail")



#and operator
# LOgical operators -> and, or, not
# percentage = 10
# if percentage >= 90 and percentage <= 100:  #and operator -> and operator ko dubai patti side ko conditions satisfy hunu parxa
#     print("A+ grade")   
# elif percentage  >= 80 and percentage < 90:
#     print("A grade")   
# elif percentage >= 70 and percentage < 80:
#     print("B+ grade")   
# elif percentage >= 60 and percentage < 70:
#     print("B grade")
# else:
#     print("Fail")
    
    
# # #  or -> Or operator kunai auta conditions satisfy bhayo bhane hunxa
# age = int(input("Enter your age:"))
# if age > 18 or age == 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")