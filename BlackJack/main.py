import random

# Ranks and Suits with Symbols
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = {
    'Spades': '♠',
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣'
}

# Welcome screen
def show_welcome():
    print(r"""
 __        __   _                            _        
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___  
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
                                                     
             🂡  Welcome to BLACKJACK! 🂱
          Try to hit 21 without going bust!
    """)

# Input prompts
def pre_pa():
    while True:
        try:
            pa = int(input("🎮 Enter total number of players (including bots): "))
            if pa < 1:
                print("❌ There must be at least 1 player.")
                continue

            re = int(input("🧍 Enter number of real (human) players: "))
            if re < 0 or re > pa:
                print("❌ Real players must be between 0 and total players.")
                continue

            rou = int(input("🔁 How many rounds would you like to play?: "))
            if rou < 1:
                print("❌ Rounds must be at least 1.")
                continue

            return pa, re, rou

        except ValueError:
            print("❌ Please enter a valid number.")

# Generate 52-card deck
def generate_deck():
    return [
        f"{rank} of {suit}"
        for suit in suits
        for rank in ranks
    ]

# Visual formatting of card
def format_card_visual(card):
    rank, suit_name = card.split(" of ")
    suit_symbol = suits[suit_name]
    if len(rank) == 2:
        return f"│{rank}     {suit_symbol}│"
    else:
        return f"│{rank}      {suit_symbol}│"

# Deal cards
def card_giving(deck, num_cards=2):
    return random.sample(deck, num_cards)

# Distribute and display hands (with dynamic player names)
def card_pay(pa, re, deck):
    players = {}
    for i in range(1, pa + 1):
        # Name human players
        if i <= re:
            if re == 1:
                player_type = "You"
            else:
                player_type = f"Player {i}"
        else:
            player_type = f"Bot {i - re}"

        cards = card_giving(deck, 2)
        players[player_type] = cards

        print(f"\n🎴 {player_type} was dealt:")
        for card in cards:
            print(format_card_visual(card))
            deck.remove(card)

    return players

# Calculate hand value
def calculate_hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        rank = card.split(" ")[0]
        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
            aces += 1
        else:
            total += int(rank)

    # Adjust for Aces if busting
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

# Decide winner(s)
def decide_winner(players):
    scores = {}

    for name, hand in players.items():
        total = calculate_hand_value(hand)
        if total > 21:
            print(f"{name} busted with {total} ❌")
        else:
            print(f"{name} has {total} 🟢")
            scores[name] = total

    if not scores:
        print("\n😵 All players busted. No winners.")
        return

    max_score = max(scores.values())
    winners = [name for name, score in scores.items() if score == max_score]

    print("\n🎉 Winner(s):")
    for winner in winners:
        print(f"🏆 {winner} with {max_score} points")

# Main game loop
def main():
    show_welcome()
    pa, re, rou = pre_pa()

    for round_number in range(1, rou + 1):
        print(f"\n===== 🃏 ROUND {round_number} =====")
        deck = generate_deck()
        players = card_pay(pa, re, deck)
        decide_winner(players)

if __name__ == "__main__":
    main()
