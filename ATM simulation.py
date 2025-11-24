def authenticate(correct_pin, max_attempts=3):

    #asks user to enter the correct pin
    #gives it 3 tries; if all 3 fail denies the access
        
    while max_attempts > 0:
        get_pin = input("Enter your pin: ")
        max_attempts -= 1
        if get_pin == correct_pin:
            return True
        else:
            if max_attempts > 0:
                print(f"Invalid pin! You have {max_attempts} attempts left. Try again.") 

    print("Too many incorrect attempts. Access denied.")
    return False  

def show_menu():

    #just prints the menu options
    print("\nMenu:")
    print("1 - Check balance")
    print("2 - Deposit money")
    print("3 - Withdraw money")
    print("4 - Exit")

def get_amount(prompt):

    #makes sure that input is a number (float)
    #doesn't allow negative values
    
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Error. Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Error. You need to enter a number")        
            
def main():

    #balance is set to 0 so it can be updated
    #previous functions are called
    #allows the user to choose a number from menu and either shows, updates the balance or exits the program
    
    balance = 0.0
    correct_pin = "1234"
    check_pin = authenticate(correct_pin) #saves/stores only the return value from a function
    if check_pin:
        print("Logged in!")
        while True:
            show_menu()
            choice = input("Pick an option: ")
            if choice == "1":
                print(f"Your current balance is {balance}")
                input("\nPress Enter to return to the menu.")
            elif choice == "2":
                amount = get_amount("Enter the amount: ")
                balance += amount
                print(f"You deposited {amount}$. Your current balance is: {balance}$")
                input("\nPress Enter to return.")  
            elif choice == "3":
                withdraw = get_amount("Enter the amount you wish to withdraw: ")
                if withdraw > balance:
                    print("Insufficient funds. Transaction cancelled.")
                else:
                    balance -= withdraw
                    print(f"Your current balance is {balance}$. You withdrew: {withdraw}$")
                input("Press Enter to return.")         
            elif choice == "4":
                print("Thank you for using our ATM services!")
                break
            else:
                print("\nInvalid choice. Choose 1, 2, 3 or 4.")    
    else:
        print("Goodbye.")    
    return

if __name__ == "__main__":
    main()
