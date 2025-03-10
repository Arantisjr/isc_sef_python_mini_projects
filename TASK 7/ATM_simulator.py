ini_balance = 20000
user_input=int(input("enter your choice 1.deposit 2.withdraw 3.acc bance 4.exit:"))



if user_input==1:
    add_funds = int(input("Enter deposit amount: "))
    print(f"New balance:$ ${add_funds+ini_balance}")
elif user_input==2:
    withraw_funds=int(input("Enter withrawal amount: "))
    print(f"succesful withdraw:$ ${withraw_funds}")
    print(f"New balance:$ ${ini_balance - withraw_funds}")
elif user_input==3:
    print(f"current balance:$ ${ini_balance}")
else:
    print("exit")

