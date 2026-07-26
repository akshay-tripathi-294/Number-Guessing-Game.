print("Welcome to number gussing game")
import random
secret = random.randint(1,100)
chance = 5
while chance > 0:
    print("\n Remaining Chances:",chance)
    guess = int(input("Enter a number:"))
    
    if guess == secret:
        print("Congratulations! you winn")
        break
    elif guess < secret:
        print("number chota hai upr jaoo")
    else:  
         print("number bada hai niche jao")

    chance = chance-1
    if chance == 1:
        print("Alert! Only 1 Chance left!")
print("you have not any chance and,")
print("Game over")
print("secret number was:",secret)
