import random
import time
from questions import questions

SCORE_FILE = "scores.txt"


# subject selection
def choose_subject():
    subjects = ["PYTHON", "C", "C++", "DBMS", "CYBER", "MIX"]

    while True:
        print("\n********** SELECT SUBJECT **********")
        for i in range(len(subjects)):
            print(i+1, ".", subjects[i])

        choice = input("Enter choice (name or number): ").strip().upper()

        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(subjects):
                return subjects[num-1]
            else:
                print("Invalid number!")

        elif choice in subjects:
            return choice

        else:
            print("Invalid input! Try again.")


# filter
def filter_questions(subject):
    if subject == "MIX":
        return random.sample(questions, 10)
    return [q for q in questions if q["subject"] == subject]


# score save
def save_score(name, score, total):
    try:
        with open(SCORE_FILE, "a") as file:
            file.write(name + " - " + str(score) + "/" + str(total) + "\n")
    except:
        print("Error saving score!")


# leaderboard
def show_leaderboard():
    print("\n********** LEADERBOARD **********")
    try:
        with open(SCORE_FILE, "r") as file:
            print(file.read())
    except:
        print("No scores yet.")


# quiz fun
def run_quiz():
    print("Program started...\n")

    name = input("Enter your name: ").strip()

    subject = choose_subject()
    quiz_questions = filter_questions(subject)

    random.shuffle(quiz_questions)

    score = 0

    print("\n********** QUIZ START **********\n")

    for i, q in enumerate(quiz_questions, 1):
        print("********************************")
        print("Question", i, ":", q["question"])
        print("********************************")

        for opt in q["options"]:
            print(opt)

        start = time.time()

        answer = ""
        while answer not in ["A", "B", "C", "D"]:
            answer = input("Answer (A/B/C/D): ").upper().strip()
            if answer not in ["A", "B", "C", "D"]:
                print("Invalid input!")

        end = time.time()

        if end - start > 10:
            print("TIME UP!\n")
            continue

        if answer == q["answer"]:
            print("CORRECT\n")
            score += 1
        else:
            print("WRONG | Correct:", q["answer"], "\n")

    print("********************************")
    print("RESULT:", score, "/", len(quiz_questions))
    print("********************************")

    save_score(name, score, len(quiz_questions))
    show_leaderboard()


# main
if __name__ == "__main__":
    run_quiz()
