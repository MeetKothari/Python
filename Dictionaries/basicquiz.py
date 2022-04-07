# This is a simple program, which uses dictionaries and lists
# to constantly ask the user questions through the terminal.
#
# Features: dictionaries, lists, loops, I/O

def new_game():
    
    current_guesses = []
    correct_guesses = 0
    question = 1
    
    for key in questions:
        print("----------------------------")
        print(key)
        for i in answers[question - 1]:
            print(i)
            
        guess = input("\nEnter a valid answer: ")
        guess = guess.upper()
        current_guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        
        question += 1
        
    display(correct_guesses, current_guesses)
        
def check_answer(answer, guess):
    
    if answer == guess:
        print("\nCorrect! Surprisingly...")
        return 1
    else:
        print("\nWrong. As expected.")
        return 0
def display(correct_guesses, current_guesses):
    
    print("----------------------------")
    print("\nResults:")
    print("----------------------------")
    
    print("Answers: ", end = "")
    for i in questions:
        print(questions.get(i), end = "")
        
    print("Guesses: ", end = "")
    for i in current_guesses:
        print(i, end = "")
    print()
    
    score = int((correct_guesses/len(questions)) * 100)
    print("\nYour score is: " + str(score) + "%")

def play_again():
    
    response = input("\nDo you want to play again?")
    response = response.upper()
    
    if response == "YES":
        return True
    else:
        return False

questions = {
    "What is the capital of Vermont?: ": "A",
    "What is the square of 64?: ": "B",
    "Is Python a multi-paradigm language?: ": "B",
    "What's Aum's favorite color?: ": "C"
}

answers = [["A. Montpelier", "B. Nashua", "C. Boston"],
          ["A. 64", "B. 4096", "C. Math sucks...", "D. -8"],
          ["A. No", "B. Yes", "C. It depends on which IDE you use!"],
          ["A. Aum does not have a color or a soul...", "B. Black, like Aum's soul would be if he had one...", "C. Baby Blue", "D. Midnight Blue"]]

new_game()

while play_again():
    new_game()
    
print("\nBye! Thanks!")
