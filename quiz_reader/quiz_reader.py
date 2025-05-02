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

            if current_question_data:
                question_list.append(current_question_data)

    # if file is not found
    except FileNotFoundError: 
        # print the file is not found
        print(f"Error: The file '{quiz_file_path}' does not exist.")
    # if there are other errors
    except Exception as unexpected_error:
        # print the error
        print(f"Unexpected error: {unexpected_error}")

    return question_list

if __name__ == "__main__":
    quiz_file_name = 'quiz_questions.txt'
    loaded_questions = load_questions_from_file(quiz_file_name)

    print("=== Loaded Questions ===")
    for index, question_data in enumerate(loaded_questions, start=1):
        print(f"\nQuestion {index}: {question_data['question_text']}")
        print(f"  a) {question_data['option_a']}")
        print(f"  b) {question_data['option_b']}")
        print(f"  c) {question_data['option_c']}")
        print(f"  d) {question_data['option_d']}")
        print(f"Correct Answer: {question_data['correct_answer']}")

    # for each question
    def run_quiz(question_list):
        user_score = 0
        total_questions = len(question_list)

        # display question and 4 options
        for question_number, question_data in enumerate(question_list, start=1):
            print(f"\nQuestion {question_number}: {question_data['question_text']}")
            print(f"  a) {question_data['option_a']}")
            print(f"  b) {question_data['option_b']}")
            print(f"  c) {question_data['option_c']}")
            print(f"  d) {question_data['option_d']}")

            # enter the anwer
            user_answer = ""
            # except ValueError
            valid_answers = ["a", "b", "c", "d"]

            while user_answer not in valid_answers:
                user_answer = input("Your answer (a/b/c/d): ").lower().strip()
                if user_answer not in valid_answers:
                    print("Please enter a valid choice: a, b, c, or d")

            # check if it matches the correct answer
            correct_answer = question_data["correct_answer"].lower()
            # if correct
            if user_answer == correct_answer:
                # print correct
                print("Correct!")
                user_score += 1
            # if wrong
                # print wrong
        # continue