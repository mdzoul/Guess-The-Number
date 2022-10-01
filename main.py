import random
import time
from replit import clear
from art import logo

def loading(a):
    if a == "Start":
        b = "2"
    elif a == "Exit":
        b = "1"
    clear()
    logo()
    print(f"\33[3{b}m{a}ing game.\33[0m")
    time.sleep(0.5)
    clear()
    logo()
    print(f"\33[3{b}m{a}ing game..\33[0m")
    time.sleep(0.5)
    clear()
    logo()
    print(f"\33[3{b}m{a}ing game...\33[0m")
    time.sleep(0.5)
    clear()
    logo()

def refresh():
    clear()
    logo()

def lives_left(difficulty):
    global lives
    lives -= 1
    return lives

def choose_difficulty():
    difficulty_chosen = False
    while not difficulty_chosen:
        difficulty = input("Choose difficulty:\n\33[32mEasy\33[0m/\33[33mNormal\33[0m/\33[31mHard\33[0m \n").lower()
        if difficulty == 'easy':
            difficulty_chosen = True
            computer_num = random.randint(1, 20)
            refresh()
            print("\33[32m---Easy Mode---\33[0m")
            print("I am thinking of a number between 1 and 20\n")
        elif difficulty == 'normal':
            difficulty_chosen = True
            computer_num = random.randint(1, 100)
            refresh()
            print("\33[33m---Normal Mode---\33[0m")
            print("I am thinking of a number between 1 and 100\n")
        elif difficulty == 'hard':
            difficulty_chosen = True
            computer_num = random.randint(1, 1000)
            refresh()
            print("\33[31m---Normal Mode---\33[0m")
            print("I am thinking of a number between 1 and 1000\n")
        else:
            refresh()
            print("\33[31m[Invalid input]\33[0m")
    return computer_num

def game():
        end_game = False
        while not end_game:
            
            print(f"You have \33[1;31m{lives_left(lives)}\33[0m lives remaining")
            user_num = int(input("Guess a number: "))
            if user_num == computer_num:
                end_game = True
                print(f"\n\33[1;32mNice! The answer was {str(computer_num)}.\33[0m")
            elif lives == 1:
                end_game = True
                print(f"\n\33[1;31mBoo! The correct answer was {str(computer_num)}.\33[0m")
            elif user_num > computer_num:
                print("\33[1;35mToo high\33[0m\n")
            elif user_num < computer_num:
                print("\33[1;36mToo low\33[0m\n")

def restart_decision():
    decided = False
    while not decided:
        go_again = input("Wanna go again? \33[1;32mY\33[0m/\33[1;31mN\33[0m ").lower()
        if go_again == 'n':
            decided = True
            should_stop = True
            loading("Exit")
        elif go_again == 'y':
            decided = True
            should_stop = False
        else:
            refresh()
            print("\33[31m[Invalid input]\33[0m")

should_stop = False
while not should_stop:
    lives = 6
    refresh()
        
    print("Welcome to Guess The Number game!\n")
    loading("Start")

    computer_num = choose_difficulty()

    game()

    time.sleep(1.5)
    refresh()
    restart_decision()