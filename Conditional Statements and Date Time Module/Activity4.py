Number = int(input("Enter number to check :"))

if Number > 174:
    print("Number is greater then 174")
    if Number%2==0:
        print("And its even too")
    else:
        print("And its odd")
else:
    print("Number is less then 174")