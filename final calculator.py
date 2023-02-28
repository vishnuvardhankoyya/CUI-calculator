def add(number1, number2): 
    return (number1 + number2) 

print("Operation Menu -\n" \ 
        "1. Addition of two numbers\n" \ )

select = input("Select operations form 1, 2, 3, 4 :") 
  
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))

if select == '1': 
    print(num1, "+", num2, "=", 
                    add(num1, num2)) 
    
else: 
    print("Invalid input!")