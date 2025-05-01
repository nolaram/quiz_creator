# read the file
def read_and_display_quiz_file(quiz_file_path):
    try:
        # open the file
        with open(quiz_file_path, 'r', encoding='utf-8') as quiz_file:
            # read the entire content of the file
            file_contents = quiz_file.read()
        # display the file content of the file
        print(file_contents)
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
    read_and_display_quiz_file(quiz_file_name)