# read the file
def load_questions_from_file(quiz_file_path):
    question_list = []

    try:
        # open the file
        with open(quiz_file_path, 'r', encoding='utf-8') as quiz_file:
            current_question_data = {}
            # read the entire content of the file
            for line in quiz_file:
                stripped_line = line.strip()
                
    # if file is not found
    except FileNotFoundError: 
        # print the file is not found
        print(f"Error: The file '{quiz_file_path}' does not exist.")
    # if there are other errors
    except Exception as unexpected_error:
        # print the error
        print(f"Unexpected error: {unexpected_error}")

if __name__ == "__main__":
    quiz_file_name = 'quiz_questions.txt'
    loaded_questions = load_questions_from_file(quiz_file_name)