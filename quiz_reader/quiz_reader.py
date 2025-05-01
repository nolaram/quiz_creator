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
    # print the file is not found
# if there are other errors
    # print the error