def authenticate(correct_pin, max_attempts=3):

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
    print("\nMenu:")
    print("1 - Check balance")
    print("2 - Deposit money")
    print("3 - Withdraw money")
    print("4 - Exit")

def get_amount(prompt):
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
    balance = 0.0
    correct_pin = "1234"
    check_pin = authenticate(correct_pin) 
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