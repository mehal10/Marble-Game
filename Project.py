import random

def marble_betting_game():
    print("Welcome to the Marble Betting Game!")
    money = int(input("Enter total money: "))  # Starting money
    
    while money > 0:
        print(f"You have ${money}.")
        try:
            bet = int(input("Enter your bet amount (or 0 to quit): "))
            if bet == 0:
                print("Thanks for playing!")
                break
            if bet > money:
                print("You don't have enough money to place this bet!")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        marbles = ['white'] * 4 + ['black'] * 6  # 4 white, 6 black
        drawn_marble = random.choice(marbles)
        print(f"You drew a {drawn_marble} marble!")
        
        if drawn_marble == 'white':
            money += bet  # Double the bet amount
            print(f"Congratulations! You doubled your bet. You now have ${money}.")
        else:
            money -= bet  # Lose the bet amount
            print(f"Oh no! You lost your bet. You now have ${money}.")
    
    print("Game over. You're out of money!")

if __name__ == "__main__":
    marble_betting_game()
