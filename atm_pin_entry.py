"""
Assignment 4 Part 2: ATM Pin Entry
"""

#imports
import sys

def main():
    """
    Main ATM function
    """
    pin_number = '1234'
    entry_attempts = 0
    while entry_attempts < 3:
        try:
            atm_code = input('Enter your PIN number: ')
            if atm_code == pin_number:
                print('Your account balance is: $1,000,000. Thank you!')
                sys.exit()
            if not atm_code == pin_number:
                print('Invalid pin.')
        except ValueError:
            print('Invalid pin.')
        entry_attempts += 1
    print('Account locked. The police are on their way.')


if __name__ == '__main__':
    main()
