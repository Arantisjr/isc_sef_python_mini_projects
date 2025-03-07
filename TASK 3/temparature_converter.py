def temp_converter():
    temp=float(input("enter temp:"))
    choice = input("convert to C/F:")
    if choice == "C":
        print("Converted temperature:",(temp-32)*(5/9))
    elif choice == "F":
        print("Converted temperature:",(temp*(9/5)+32))


temp_converter()        