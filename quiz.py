# Define the quiz questions, options, and correct answer
questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["A. define", "B. def", "C. func", "D. function"],
        "answer": "B"
    },

    {
        "question": "Which of the following is the correct extension of the Python file?",
        "options": ["A. .python", "B. .pl", "C. .py", "D. .p"],
        "answer": "C"
    },
    {
        "question": "Which data type is mutable in Python?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Int"],
        "answer": "C"
    },
    {
        "question": "Who developed Python Programming Language?",
        "options": ["A. Wick van Rossum", "B. Guido van Rossum", "C. James Cameron", "D. Martin Scorsese"],
        "answer": "B"
    },
    {
        "question": "What symbol is used to start a comment in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. <!--"],
        "answer": "C"
    }
]

def runQuiz():
    score = 0
    print("Welcome to the quiz! Answer the questions by choosing A, B, C, or D.\n")

    # Ask each question
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()

        # Check if the answer is correct
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")
    
    # Display the score
    print(f"Your final score is {score} out of {len(questions)}.\n")

def main():
    play_again = "Y"
    while play_again.upper() == "Y":
        runQuiz()
        play_again = input("Do you want to play again? (Y/N): ")

# Start the quiz
main()
