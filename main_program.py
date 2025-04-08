# import all libraries needed for the program
# main loop for asking questions

def main():
    file_name = 'quiz_questions.txt'

    with open(file_name, 'a') as file:
        while True:
            print('-- Add a new Question --')
            question = input("Enter a question: ")
            option_a = input("Enter option A: ")
            option_b = input("Enter option B: ")
            option_c = input("Enter option C: ")
            option_d = input("Enter option D: ")
            
    # correct answer
# exit program