from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
quiz = QuizBrain(questions)

for i in range(len(question_data)):
    question = question_data[i]["text"]
    answer = question_data[i]["answer"]
    questions.append(Question(question, answer))


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print()
print(f"Your final score is {quiz.score} / {quiz.question_number}")