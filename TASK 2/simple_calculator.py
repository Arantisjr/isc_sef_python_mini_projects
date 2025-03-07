def Calc():
    a=int(input("Enter first operand:"))
    b=int(input("Enter second operand:"))
    op=input("Enter an operator(+,*,-,/,%):")
    if op == "+":
        print("Results:", a+b)
    elif op == "*":
          print("Results:", a*b)   
    elif op == "-":
          print("Results:", a-b) 
    elif op == "/":
          print("Results:", a/b)  
    elif op == "%":
          print("Results:", a%b) 



Calc()          