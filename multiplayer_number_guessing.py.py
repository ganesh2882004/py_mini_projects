import random
import os
from getpass import getpass

def clear_system ():
    os.system("cls" if os.name == "nt" else "clear")

def number_guessing_game ():

    print ("welcome to number_guessing_game" )

    players = int(input("Enter the number of players (1-4) : "))

    if players < 1 or players > 4:
        print("Invalid number of players.")
        return
    

    print ("choose your defeculty" )
    print ("1,(You have 10 chance to guess, defeculty :easy)" )
    print ("2,(You have 5 chance to guess, defeculty : medium)" )
    print ("3,(You have 10 chance to guess, defeculty :hard)" )

    choose = int(input("Enter your choice "))

    if choose == 1:
        chance = 10
        defeculty ="easy"
    elif choose == 2:
        chance = 5
        defeculty ="medium"
    elif choose == 3 :
        chance = 3
        defeculty ="hard"
    else:
        print("You enterd the wromg number(defeculty)")
        return
    
    secret_number = random.randint(1,50)
    print(f" your defeculty as choice is {defeculty }")
    print("guess  a number btw 1 to 50")


    while chance >0 :
        for players  in range(1 , players + 1 ) :
            if chance <= 0:
                break

            clear_system()

            try:
                print(f"Player {players }'s Turn")

                guess = int(getpass("enter your guess :"))
            
                if guess == secret_number:
                    print("🎉 Congratulations! You guessed correctly.")
                    return

                elif guess < secret_number:
                    print("📉 Too Low")

                else:
                    print("📈 Too High")
                chance -=1

                print(f"your remaing chance is : {chance}")
                input("\nPress Enter and pass the device to the next player...")
                
            except ValueError:
                print("Please enter a valid number.")
    
    clear_system ()
        
    print("\n💀 Game Over!")
    print(f"The correct number was {secret_number}")

number_guessing_game ()




    
