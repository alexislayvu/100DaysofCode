from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# This is where we will store the questions and answers
question_bank = []

# Add the questions and answers from data.py into question_bank
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congrats! You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")