print("Dollar","Euros","Pounds",
      "Naira")
user_rate = input("Enter your balance: ")
number = int(user_rate)
print(number)
user_convert = input("Enter the currency you balance should be converted into: ")
if user_convert == "Dollars": 
    print(number * 12)
elif user_convert == "Euros":
    print(number * 13)
elif user_convert == "Pounds":
    print(number * 15)
elif user_convert == "Naira": 
    print(number * 100)
else:
    print("Unable to convert")    