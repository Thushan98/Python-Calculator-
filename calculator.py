def add (num1, num2):
  return num1+num2
def subtract (num1, num2):
  return num1-num2
def multiply (num1, num2):
  return num1*num2
def divide (num1, num2):
    if num2 == 0:
        print("float division by zero")
    else:
        return num1/num2
  
def power (num1, num2):
  return num1**num2
def remainder (num1, num2):
  return num1%num2
def reset(num1,num2):
    num1=""
    num2=""
    return
def select_op(choice):
    if choice =='+':
      print(number1,'+', number2,  '=', add(number1,number2) )
    elif choice =='-':
      print(number1, "-", number2, " = ", subtract(number1,number2) )
    elif choice =='*':
      print(number1, "*", number2, " = ", multiply(number1,number2) )  
    elif choice =='/':
      print(number1, "/", number2, " = ", divide(number1,number2) )
    elif choice =='^':
      print(number1, "^", number2, " = ", power(number1,number2) )
    elif choice =='%':
      print(number1, "%", number2, " = ", remainder(number1,number2) )
      
    elif choice =='$':
      print(reset(number1,number2) )
    
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")


  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")

  if choice in ["+","-","*","/","^","%","$"]:
     
    number1= float(input("Enter first number: "))
    number2= float(input("Enter second number: "))
    select_op(choice) 
  else:
    print("Done. Terminating")
    break
    exit()