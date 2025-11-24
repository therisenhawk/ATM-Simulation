# ATM Simulation

This is a simple ATM simulation written in Python.  
It runs in the terminal and lets a user log in with a PIN, check their balance, deposit money, and withdraw money.

I built this project to practice:

- Functions
- While loops
- Input validation with `try` / `except`
- Basic program structure with a `main()` function

---

## How it works

- The program uses a fixed PIN: **1234**
- The user gets **3 attempts** to enter the correct PIN  
  - If all attempts fail, access is denied and the program exits
- After a successful login, the user sees a menu:

  1. Check balance  
  2. Deposit money  
  3. Withdraw money  
  4. Exit  

- The starting balance is **0.0**

### Features

- **Login system**
  - Simple PIN check with a maximum number of attempts

- **Check balance**
  - Shows the current account balance
  - Waits for the user to press Enter before returning to the menu

- **Deposit**
  - Asks the user how much they want to deposit
  - Only accepts positive numbers
  - Invalid input (like letters or negative values) is handled with an error message

- **Withdraw**
  - Asks the user how much they want to withdraw
  - Only accepts positive numbers
  - Checks if there are enough funds in the account
  - If there isn’t enough balance, the withdrawal is cancelled

- **Exit**
  - Ends the program with a short goodbye message


