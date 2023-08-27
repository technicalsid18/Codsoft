class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def check_answer(self, user_choice):
        return user_choice == self.correct_choice

def run_quiz(questions):
    score = 0
    for idx, question in enumerate(questions, start=1):
        print(f"Question {idx}: {question.text}")
        for choice_idx, choice in enumerate(question.choices, start=1):
            print(f"{choice_idx}. {choice}")
        user_choice = int(input("Enter your choice (1, 2, 3, ...): "))
        
        if 1 <= user_choice <= len(question.choices):
            if question.check_answer(user_choice):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question.correct_choice}\n")
        else:
            print("Invalid choice. Moving on to the next question.\n")
    
    print(f"Quiz completed! Your score: {score}/{len(questions)}")

def main():
    question1 = Question("What is the capital of France?", ["Paris", "London", "Berlin"], 1)
    question2 = Question("Which planet is known as the Red Planet?", ["Saturn", "Mars", "Venus"], 1)
    question3 = Question("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Charles Dickens", "Jane Austen"], 1)
    question4 = Question("What is the capital of Japan?", ["Tokyo", "Seoul", "Beijing"], 1)
    question5 = Question("Which gas is most abundant in Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide"], 1)
    question6 = Question("Which planet is closest to the Sun?", ["Venus", "Mercury", "Mars"], 2)
    question7 = Question("What is the chemical symbol for gold?", ["Au", "Ag", "Fe"], 1)
    question8 = Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"], 1)

    questions = [question1, question2, question3, question4,question5,question6,question7,question8]
    run_quiz(questions)

if __name__ == "__main__":
    main()
