class QuizGame:
    def __init__(self):
        self.questions = [  # 'self.questions' refers to the instance variable 'questions'
            "What is the capital of France?",
            "What is 2 + 2?",
            "What is the capital of Spain?",
            "What is the largest planet in our solar system?"
        ]
        self.answers = [  # 'self.answers' refers to the instance variable 'answers'
            "Paris",
            "4",
            "Madrid",
            "Jupiter"
        ]
        self.prize = 0  # 'self.prize' refers to the instance variable 'prize'
        self.prize_per_question = 100  # 'self.prize_per_question' refers to the instance variable 'prize_per_question'

    def ask_question(self, question, correct_answer):
        user_answer = input(question + " ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            self.prize += self.prize_per_question  # 'self.prize' refers to the instance variable 'prize'
        else:
            print("Incorrect. The correct answer was:", correct_answer)

    def play_game(self):
        for i in range(len(self.questions)):
            self.ask_question(self.questions[i], self.answers[i])  # 'self.questions' and 'self.answers' refer to the instance variables

        print("Game over!")
        print("You are taking home $", self.prize)  # 'self.prize' refers to the instance variable 'prize'
#print(__name__)
if __name__ == "__main__":
    print(__name__)
    game = QuizGame()  # Create an instance of 'QuizGame'
    game.play_game()  # Call the 'play_game' method on the instance
