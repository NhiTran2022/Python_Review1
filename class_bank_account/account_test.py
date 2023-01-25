# This program demonstrates the BankAccount class.

import bankaccount

def main():

    # get the starting balance.
    start_bal = float(input("Enter your starting balance: "))

    # Create a BankAccount object
    saving = bankaccount.BankAccount(start_bal)

    # Deposit the user's paycheck.
    check = float(input("How much were you paid this week? "))
    print("I will deposit that into your account.")
    saving.deposit(check)

    # Display the balance.
    # print("Your balance is $", format(saving.get_balance(), ',.2f'), sep='')
    print(saving)
    # Get the amount to withdraw.
    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account.")
    saving.withdraw(cash)

    # Display the balance.
    # print("Your account balance is $", format(saving.get_balance(), ',.2f'),sep='')
    print(saving)
    
# Call the main function.
main()