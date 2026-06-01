import random

def number_guessing_game():
    print("welcome to number_guessing_game")
    print("choose your defeculty")
    print("1,easy (10 chance to guess)")
    print("2. Medium (5 Chances to guess)")
    print("3. Hard (3 Chances to guess)")
    choose = int(input("choose 1,2 or 3 : "))

    if choose ==1:
        chance =10
        defeculty="easy"
    elif choose == 2:
        chance =5
        defeculty="Medium"
    elif choose == 3:
        chance =3
        defeculty="Hard "
    else: 
    
        print("Invalid choice")
        return
    
    scecret_number=random.randint(1,50)
    print(f"\nYou chose the difficulty level: {defeculty}")
    print("Guess the number btw 1 to 50")
     
    while chance > 0:
        try:
            guess=int(input("enter your guess"))

            if guess == scecret_number :
                 print("🎉 Congratulations! You guessed correctly.")
                 return
            elif guess < scecret_number :
                
                print("📉 Too Low")

            else:
                print("📈 Too High")
            chance -=1
            print(f"Remaining Chances: {chance}")
        
        except ValueError:
            print("❌ Please enter a valid number")
    print("\n💀 Game Over!")
    print(f"The correct number was {scecret_number}")   
        
        
            
        




number_guessing_game()
