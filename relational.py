# Relational Operator in Python

# ==   Equal to              → x == y
# !=   Not equal to          → x != y
# >    Greater than          → x > y
# <    Less than             → x < y
# >=   Greater than or equal → x >= y
# <=   Less than or equal    → x <= y


slot_machine_ascii = r"""
🎰🎰🎰 Joker Lucky 🎰🎰🎰
+------------------------+
| [0]  [0]  [0]          |
| [0]  [?]  [0]          |
| [0]  [0]  [0]          |
+------------------------+
  🎲 Try Your Luck! 🎲
"""

try:
    import os
    import random
    import time
except ImportError as e:
    print("A required module could not be imported:", e)


def random_number_generator(wallet):
    print("\nGuess a number between 1 and 20")
    response2 = int(input("Input your number: "))
    random_number = random.randint(1, 20)
    print("Our Lucky number was", random_number)
    
    if response2 == random_number:
        print("🎉 You win 100 USD!")
        wallet += 100
    else:
        print("❌ You lose 100 USD.")
        wallet -= 100

    print('💰 Your wallet:', wallet)
    return wallet


def game_engine(wallet):
    while wallet >= 100:
        print('\n💵 Current wallet:', wallet)
        wallet = random_number_generator(wallet)
        if wallet < 100:
            print("\n⚠️ Wallet dropped below 100 USD. Returning to main menu.")
            break
    return wallet


def main():
    print(slot_machine_ascii)
    print('🎉 Welcome to Joker Lucky Game 🎉')
    print("""Game rules:
    - Guess a number from 1 to 20.
    - Match the lucky number to win 100 USD.
    - If you fail, you lose 100 USD.
    - Minimum 100 USD needed to play.
    """)
    
    wallet = int(input('💼 Input your wallet amount: '))
    
    while True:
        response = input('\n▶️ Do you want to start playing? (y/n): ').lower()
        
        if response == 'y':
            wallet = game_engine(wallet)
            # After game ends, ask if they want to top-up or exit
            if wallet < 100:
                print("\n🛑 You ran out of money to continue.")
                wallet = int(input("💸 Please input new wallet amount to play again: "))
        elif response == 'n':
            print("👋 Thanks for visiting Joker Lucky. Goodbye!")
            break
        else:
            print("⚠️ Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
