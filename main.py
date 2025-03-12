import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_round():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    return determine_winner(user_choice, computer_choice)

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds would you like to play? "))
    
    for _ in range(rounds):
        result = play_round()
        print(result)
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")
    
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer wins the game! Better luck next time.")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    main()
