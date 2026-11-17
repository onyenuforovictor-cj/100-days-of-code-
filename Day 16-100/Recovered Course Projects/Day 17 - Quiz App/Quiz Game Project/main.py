from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    correct_answer = question['answer']
    new_question = Question(question = question_text, answer = correct_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.new_question()
print("you have completed the quiz")
print(f"your final score is :{quiz.score} / {quiz.question_number}")


