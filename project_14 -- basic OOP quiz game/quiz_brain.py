class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer =  current_question.answer
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {current_question.question}? (True or False): ")
        if answer == correct_answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}!")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("You got it wrong...")
            print(f"The correct answer was: {correct_answer}!")
            print(f"Your current score is: {self.score}/{self.question_number}")
    
        if self.question_number >= len(self.question_list):
            print("Game Over")
            return ""