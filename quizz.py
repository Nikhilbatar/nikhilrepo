def run_quiz():
    questions = [
        {"question": "What programming language is this code written in?\nprint('Hello, World!')", "options": ["Python", "Java", "C++", "JavaScript"], "answer": "Python"},
        {"question": "Which programming language uses curly braces {} to define code blocks?", "options": ["Python", "Java", "C++", "JavaScript"], "answer": "Java"},
        {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Level Text Manipulation Language", "Hyper Transfer Markup Language", "High Level Transfer Markup Language"], "answer": "Hyper Text Markup Language"}
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")
        user_answer = input("Your answer (enter the option number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(q['options']):
            user_answer = q['options'][int(user_answer) - 1]

        if user_answer.lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"You scored {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
