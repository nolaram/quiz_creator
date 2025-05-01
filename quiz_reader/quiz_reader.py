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

                if stripped_line.startswith("Question: "):
                    if current_question_data:
                        question_list.append(current_question_data)
                        current_question_data = {}

                    question_text = stripped_line[len("Question: "):]
                    current_question_data["question_text"] = question_text
                
                elif stripped_line.startswith("a) "):
                    current_question_data["option_a"] = stripped_line[len("a) "):]
                
                elif stripped_line.startswith("b) "):
                    current_question_data["option_b"] = stripped_line[len("b) "):]

                elif stripped_line.startswith("c) "):
                    current_question_data["option_c"] = stripped_line[len("c) "):]

                elif stripped_line.startswith("d) "):
                    current_question_data["option_d"] = stripped_line[len("d) "):]

                elif stripped_line.startswith("Correct Answer: "):
                    correct_answer = stripped_line[len("Correct Answer: "):]
                    current_question_data["correct_answer"] = correct_answer

                elif stripped_line == '-' * 40:
                    continue

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