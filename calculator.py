
while True :
    
    print(".....CALCULATOR..... \n")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Power")
    print("7. Quotient")
    print("8. Odd/Even Check")
    print("9. Exit \n")
    
    choice = int(input("Enter your Choice(1-9):"))
    
    if choice <= 0 or choice > 9: 
        print("Invalid Choice")
        break 
    
    
    if choice == 9 :
        print("Exit")
        break
    
    elif choice == 8 :
        n = int(input("Enter the number: "))
        
        if n %2 == 0 :
          print(f"{n} is even number") 
          
        else:
            print(f"{n} is odd number") 
                    
    elif choice >=1 or choice <=7:
            
        n1 = int(input("Enter First number: "))
        n2 = int(input("Enter Second number: "))
        

        if choice == 1:
            add = n1 + n2
            print("Sum is ",add)
        
        
        if choice == 2:
            sub = n1 - n2
            print("Substraction is ",sub)
            
        if choice == 3:
            mul = n1 * n2
            print("Substraction is ",mul)
        
        if choice == 4:
            div = n1 / n2
            print("Division is ",div)

        if choice == 5:
            rem = n1 % n2
            print("Remainder is ",rem)
            
        if choice == 6 :
            pow = n1 ** n2
            print("Power is ",pow)

        if choice == 7:
            quo = n1 // n2
            print("Quotient is ",quo)
            
        
    
     
        
