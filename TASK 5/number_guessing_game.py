import random
count = 0
num = random.randint(1,100)
while 1:
    users_num = int(input("Guess the number(1 to 100): "))
    count+=1
    if users_num > num:
        print("Too high, try agin")
    elif users_num < num:
        print("Too low, try again")
    elif users_num == num :
       break  

print(f"congratulations! You guesed it in {count - 1} attemps")



