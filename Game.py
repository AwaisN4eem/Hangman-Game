import random
import turtle
from colorama import Fore, Style

# Set up the turtle
hangman = turtle.Turtle()
hangman.speed(0)
hangman.penup()
hangman.ht()
hangman.pensize(5)

# Set up the hangman parts
parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

# Set up the colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set up the word list
word_list = ['corolla', 'markx', 'vigo', 'tundra', 'raptor', 'G-wagon', 'accord']

def choose_word():
    return random.choice(word_list)

def draw_gallows():
    hangman.penup()
    hangman.goto(-200, -200)
    hangman.pendown()
    hangman.forward(200)
    hangman.right(90)
    hangman.forward(300)
    hangman.right(90)
    hangman.forward(100)
    hangman.right(90)
    hangman.forward(50)

def draw_head():
    hangman.penup()
    hangman.goto(-200, 50)
    hangman.pendown()
    hangman.circle(25)
def draw_smiley_face():
    # Draw the smiley face
    hangman.penup()
    hangman.goto(-200, 50)
    hangman.pendown()
    hangman.setheading(0)
    hangman.color("black", "yellow")
    hangman.begin_fill()
    hangman.circle(50)
    hangman.end_fill()

    # Draw the eyes
    hangman.penup()
    hangman.goto(-220, 80)
    hangman.pendown()
    hangman.setheading(-60)
    hangman.circle(10, 120)

    hangman.penup()
    hangman.goto(-180, 80)
    hangman.pendown()
    hangman.setheading(-120)
    hangman.circle(10, 120)

    # Draw the mouth
    hangman.penup()
    hangman.goto(-220, 20)
    hangman.pendown()
    hangman.setheading(-60)
    hangman.circle(30, 120)
def draw_body():
    hangman.penup()
    hangman.goto(-200, 50)
    hangman.pendown()
    hangman.forward(100)

def draw_left_arm():
    hangman.penup()
    hangman.goto(-200, 0)
    hangman.pendown()
    hangman.right(45)
    hangman.forward(75)
    hangman.backward(75)

def draw_right_arm():
    hangman.penup()
    hangman.goto(-200, 0)
    hangman.pendown()
    hangman.left(45)
    hangman.forward(75)
    hangman.backward(75)

def draw_left_leg():
    hangman.penup()
    hangman.goto(-200, -50)
    hangman.pendown()
    hangman.right(45)
    hangman.forward(75)
    hangman.backward(75)

def draw_right_leg():
    hangman.penup()
    hangman.goto(-200, -50)
    hangman.pendown()
    hangman.left(45)
    hangman.forward(75)
    hangman.backward(75)

def draw_hangman_part(part_index):
    draw_functions = [draw_head, draw_body, draw_left_arm, draw_right_arm, draw_left_leg, draw_right_leg]
    draw_functions[part_index]()
turtle.bgcolor("lightcyan")
# Rest of the code...

def show_menu():
    print(f"{Fore.YELLOW}╔════════════════════════════════╗")
    print(f"║{Fore.CYAN}         Hangman Game           {Fore.YELLOW}║")
    print(f"╠════════════════════════════════╣")
    print(f"║{Fore.GREEN}      Press 'P' to Play         {Fore.YELLOW}║")
    print(f"║{Fore.BLUE}      Press 'I' for Instructions{Fore.YELLOW}║")
    print(f"║{Fore.RED}      Press 'E' to Exit         {Fore.YELLOW}║")
    print(f"╚════════════════════════════════╝")
    print(Style.RESET_ALL)



def show_instructions():
    print("Instructions:")
    print("--------------")
    print("The objective of the game is to guess the word.")
    print("You can enter one letter at a time.")
    print("If the letter is in the word, it will be revealed.")
    print("If the letter is not in the word, a part of the hangman figure will be drawn.")
    print("You have a limited number of incorrect guesses before the hangman is complete.")
    print("Good luck!")

def play_hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    while incorrect_guesses < len(parts):
        print("\nGuessed letters:", guessed_letters)
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "
        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Enter a letter to guess name of car: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                draw_hangman_part(incorrect_guesses)
                incorrect_guesses += 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

    if incorrect_guesses == len(parts):
        print("\nGame over! The word was", word)

    turtle.done()


def hangman_game():
    while True:
        show_menu()
        choice = input("Enter your choice: ").lower()

        if choice == "p":
            draw_gallows()
            play_hangman()
            break
        elif choice == "i":
            show_instructions()
        elif choice == "e":
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please try again.")


print("Welcome to Hangman Game!")
hangman_game()
