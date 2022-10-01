import random
from replit import clear
from art import logo

def lives_left(difficulty):
    global lives
    lives -= 1
    return lives

should_stop = False
while not should_stop:
    clear()
    logo()
    computer_num = random.randint(1, 100)
    
    print("""Welcome to Guess The Number game!
I am thinking of a number from 1 to 100.
""")
    
    difficulty = input("Choose difficulty:\n\33[32mEasy\33[0m/\33[31mHard\33[0m ").lower()
    clear()
    logo()
    if difficulty == 'easy':
        lives = 11
        print("\33[32m---Easy Mode---\33[0m")
    elif difficulty == 'hard':
        lives = 6
        print("\33[31m---Hard Mode---\33[0m")
    
    end_game = False
    while not end_game:
        
        print(f"You have {lives_left(lives)} attempts remaining")
        user_num = int(input("Guess a number: "))
        if user_num == computer_num:
            end_game = True
            print(f"\nYou got it! The answer was {str(computer_num)}")
        elif lives == 1:
            end_game = True
            print(f"\nYou lost! The correct answer was {str(computer_num)}")
        elif user_num > computer_num:
            print("Too high\n")
        elif user_num < computer_num:
            print("Too low\n")
            
    if input("\nDo you want to play another round? Y/N ").lower() == 'n':
        should_stop = True
    