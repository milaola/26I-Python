
import json
import random


def load_questions():
    """Load questions from the JSON file."""
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            questions = json.load(file)

        if not isinstance(questions, list) or not questions:
            raise ValueError("The file must contain a non-empty list of questions.")

        for item in questions:
            if not isinstance(item, dict):
                raise ValueError("Each question must be an object.")

            if not all(key in item for key in (
                "question", "choices", "answer"
            )):
                raise ValueError("A question is missing required fields.")

            if not isinstance(item["choices"], dict):
                raise ValueError("Question choices must be an object.")

            if set(item["choices"]) != {"A", "B", "C", "D"}:
                raise ValueError("Each question must have choices A, B, C, and D.")

            if item["answer"] not in item["choices"]:
                raise ValueError("A question has an invalid correct answer.")

        return questions

    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Error loading questions: {error}")
        return []


def run_quiz():
    """Run the quiz and calculate the final score."""
    questions = load_questions()

    if not questions:
        print("The quiz cannot start without valid questions.")
        return

    random.shuffle(questions)
    score = 0

    print("\n" + "=" * 35)
    print("       COMMAND-LINE QUIZ")
    print("=" * 35)
    print("Answer each question using A, B, C, or D.")

    for number, item in enumerate(questions, start=1):
        print(f"\nQuestion {number}/{len(questions)}")
        print(item["question"])

        for letter, choice in item["choices"].items():
            print(f"{letter}. {choice}")

        while True:
            try:
                answer = input("Your answer: ").strip().upper()

                if answer not in item["choices"]:
                    raise ValueError("Please enter A, B, C, or D.")

                break

            except ValueError as error:
                print(error)

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {item['answer']}.")

    total = len(questions)
    percentage = (score / total) * 100

    print("\n" + "=" * 35)
    print("           QUIZ RESULTS")
    print("=" * 35)
    print(f"Your score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Excellent! You really know your stuff.")
    elif percentage >= 50:
        print("Good! Keep practising.")
    else:
        print("Try Again! Review the questions and improve.")

    print("=" * 35)

if __name__ == "__main__":
    run_quiz()
