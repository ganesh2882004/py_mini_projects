balance = 10000
pin = 1234
history = []
def ATM_Simulator ():
    
    def Check_Balance():
        print (f"your ac balance is {balance}")

    def Deposit_Money () :
        global balance
        Deposit = int(input("Enter the amount u wnat to deposit"))
        balance = balance + Deposit
        history.append(f"deposited ₹{Deposit}")
        print(f"₹{Deposit} Deposited successfully.")

    def Withdraw_Money():
        global balance

        Withdraw = int(input("Enter the amount u want to Withdraw: "))

        if balance - Withdraw >= 200:

            balance = balance - Withdraw

            history.append(f"Withdrawn ₹{Withdraw}")

            print(f"₹{Withdraw} withdrawn successfully.")

        else:
            print("Minimum balance of ₹200 must be maintained.")
    
    def Transaction_History() :
        if len(history) == 0:
            print(" no transaction found ")
        else:
            print("\nTransaction History:")

            for transaction in history:
                print(transaction)
        
    
    print("welcome to Simulator atm bank")
    user_pin = int(input("PLEASE ENTER YOUR PIN : ")) 
    
    while True:
        

        if user_pin != pin :
            print("PLEASE ENTER THE CORRECT PIN : ")
            return ATM_Simulator ()
        else:
            print("who can i help you")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Exit")
            choice = int(input("please select what do you want from the menue  : "))

        if choice == 1:
            Check_Balance ()
        elif choice == 2:
            Deposit_Money ()
        elif choice == 3:
            Withdraw_Money ()
        elif choice == 4:
            Transaction_History()
        elif choice == 5:
            print("Thank you for using ATM Simulator.")
            break
        else :
            print("Invalid choice. Please try again.")

ATM_Simulator ()    





        



