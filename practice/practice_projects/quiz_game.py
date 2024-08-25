print("***********************")
print("Welcome to My Quiz Game")

question_bank = [
    {"question":"The ability of one class to aquire methods and attributes of another class is called _______", "answer":"A"},
    {"question":"Which of the following is a type of inheritance?", "answer":"D"},
    {"question":"What type of inheritance has multiple subclasses to a single superclass?", "answer":"C"},
    {"question":"What is the depth of multilevel inheritance in python?", "answer":"C"},
    {"question":"What does MRO stands for?", "answer":"B"}
]

options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
    ["A. Single", "B. Double", "C. Multiple", "D. Both A and C"],
    ["A. Multiple Inheritance", "B. Multilevel Inheritance", "C. Heirarchical Inhertance", "D. None of these"],
    ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
    ["A. Mehtod Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order", "D. Method Resolution Object"]
]

def check_answer(user_ans, answer):
    if user_ans == answer:
        return True
    else:
        return False

qsn_no = len(question_bank)
i = 0
score = 0

while qsn_no != 0 :
    
    print("***********************")
    
    question = question_bank[i]["question"]
    answer = question_bank[i]["answer"]
    
    print(question)
    for op in options[i]:
        print(op)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    is_right = check_answer(user_answer, answer)
    
    if is_right:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is: {answer}")
    
    print(f"Your current score is {score}/{i+1}")
    
    i += 1
    qsn_no -= 1
    
print(f"\nYou have given {score} correct answers")

score_percentage = (score/i)*100

print(f"Your score is {score_percentage}%")