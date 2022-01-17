celsius = float(input("Please enter the temperature in celsius"))

fahrenheit = (celsius * 1.8) + 32
print('%0. If degree Celsius is equal to %0. If degree Fahrenheit' %(celsius,fahrenheit))
temp = fahrenheit

if (temp >= 104):
    print("It's so hot")
elif (temp <= 50):
    print("It's so cold")
else:
    print("The temperature is nice")        