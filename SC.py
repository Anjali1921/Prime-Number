def Profit(SP, CP):
    return SP-CP

def Loss(CP, SP):
    return CP - SP

def Discount(MP, SP):
    return MP-SP

def MarkedPrice(Discount, SP):
    return Discount+SP

print("Select operation.")
print("1.Profit")
print("2.Loss")
print("3.Discount")
print("4.MarkedPrice")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "-", num2, "=", Profit(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Loss(num1, num2))

        elif choice == '3':
            print(num1, "-", num2, "=", Discount(num1, num2))

        elif choice == '4':
            print(num1, "+", num2, "=", MarkedPrice(num1, num2))
      
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")