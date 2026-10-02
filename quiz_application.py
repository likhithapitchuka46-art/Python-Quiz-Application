print("================================")
print("       WELCOME TO THE QUIZ       ")
print("================================")

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which language is mainly used for Data Science?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. C"],
        "answer": "A"
    },
    {
        "question": "3. What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Unit",
            "D. Computer Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. &"],
        "answer": "B"
    },
    {
        "question": "5. Which of the following is a programming language?",
        "options": ["A. Python", "B. HTML", "C. HTTP", "D. URL"],
        "answer": "A"
    }
]

score = 0

for item in questions:
    print("\n" + item["question"])

    for option in item["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", item["answer"])

print("\n================================")
print("          QUIZ COMPLETED")
print("================================")

print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Your Percentage:", percentage, "%")