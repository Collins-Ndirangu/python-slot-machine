import random
import winsound
import os

def spin_row():
    symbols = ['🍒', '🍉', '🍌', '⭐', '🔔']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        multiplier = get_symbol_multiplier(row[0])
        return bet * multiplier
    return 0

def get_symbol_multiplier(symbol):
    multipliers = {
        '🍒': 10,
        '🍉': 20,
        '🍌': 30,
        '⭐': 40,
        '🔔': 50
    }
    return multipliers.get(symbol, 0)

def spin_grid():
    return [spin_row() for _ in range(3)]

def print_grid(grid):
    print("*******************")
    for row in grid:
        print(" | ".join(row))
    print("*******************")

def play_sound(sound_type):
    sounds = {
        'spin': (500, 100),  # (frequency, duration)
        'win': (1000, 500),
        'lose': (200, 300)
    }
    try:
        frequency, duration = sounds.get(sound_type, (500, 100))
        winsound.Beep(frequency, duration)
    except:
        pass  # Silently fail if sound can't be played

def main():
    balance = 100
    max_balance = balance
    total_spins = 0
    total_wins = 0

    print("*************************")
    print("Welcome to Python Slots  ")
    print("Symbols: 🍒 🍉 🍌 ⭐ 🔔")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        print(f"Highest balance: ${max_balance}")
        print(f"Win rate: {(total_wins/total_spins)*100:.1f}%" if total_spins > 0 else "Win rate: 0%")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number!!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!!")
            continue
        if bet <= 0:
            print("Bet amount must be greater than 0!!")
            continue

        balance -= bet

        grid = spin_grid()
        print("Spinning...\n")
        print_grid(grid)

        payout = get_payout(grid[0], bet)

        if payout > 0:
            print(f"You won ${payout}!")
            balance += payout
            total_wins += 1
            max_balance = max(max_balance, balance)
        else:
            print("Better luck next time!")

        total_spins += 1

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    # Final statistics
    print("\n******* GAME STATISTICS *******")
    print(f"Total spins: {total_spins}")
    print(f"Total wins: {total_wins}")
    print(f"Win rate: {(total_wins/total_spins)*100:.1f}%" if total_spins > 0 else "Win rate: 0%")
    print(f"Highest balance achieved: ${max_balance}")
    print("******************************")

if __name__ == '__main__':
    main()