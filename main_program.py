# import all libraries needed for the program
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
                correct_answer = input("Enter the correct answer (a/b/c/d): ")

# exit program