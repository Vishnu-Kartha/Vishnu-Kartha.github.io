class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.q_num == len(self.q_list):
            print(f"You finished the quiz: Your score is {self.score}/{len(self.q_list)}")
            return False
        else:
            return True

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print(f"You got it right! Your score is {self.score}/{len(self.q_list)}")
        else:
            print(f"You got it wrong! Your score is {self.score}/{len(self.q_list)}")


    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}.{current_question.text} True/False?")
        self.check_answer(user_answer, current_question.answer)
