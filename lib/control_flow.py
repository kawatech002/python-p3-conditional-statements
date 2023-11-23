#!/usr/bin/env python3

# control_flow.py

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"



def hows_the_weather(temperature):
    if temperature <40:
        return "it's brisky out there"
    elif temperature >=40 and temperature <=65:
        return "it's a little chilly out there"
    elif temperature > 85:
        return "it's dang too hot out there"
    else:
        return "it's perfect out there"
    


    

def fizzbuzz(num):
  if num % 3 == 0 and num % 5 ==0:
      return "FizzBuzz"
  elif num % 3== 0:
      return "Fizz"
  elif num % 5==0:
      return "Buzz"
  else:
      return num


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 !=0:
            return num1 / num2
        else:
            print("Error: Division by zero")
            return None
    else:
        print("Invalid operation!")
        return None
            
    
