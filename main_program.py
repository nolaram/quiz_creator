# import all libraries needed for the program
from colorama import Fore, Style, init

init(autoreset=True)

# main loop for asking questions
def main():
    file_name = 'quiz_questions.txt'

    with open(file_name, 'a') as file:
        # options
        while True:
            print('-- Add a new Question --')
            question = input("Enter a question: ")
            option_a = input("Enter option A: ")
            option_b = input("Enter option B: ")
            option_c = input("Enter option C: ")
            option_d = input("Enter option D: ")

            # correct answer
            correct_answer = input("Enter the correct answer (a/b/c/d): ").lower()
            while correct_answer not in ['a', 'b', 'c', 'd']:
                print("Invalid input! The answer must be (a/b/c/d)")
                correct_answer = input("Enter the correct answer (a/b/c/d): ").lower()

            # write the input in the file
            file.write(f'Question: {question}\n')
            file.write(f'a) {option_a}\n')
            file.write(f'b) {option_b}\n')
            file.write(f'c) {option_c}\n')
            file.write(f'd) {option_d}\n')
            file.write(f'Correct Answer: {correct_answer}\n')
            file.write('-' * 40 + '\n')

            # ask user if he/she wants to add another question
            repeat = input("Do you want to add another question? (yes/no): ").strip().lower()
            if repeat != 'yes':
                print("Thank you!")
                # exit program
                break

# go back to main
if __name__ == '__main__':
    main()