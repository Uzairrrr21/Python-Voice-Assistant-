import random

# Define question categories and difficulty levels
categories = {
    "math": ["arithmetic", "algebra", "geometry"],
    "science": ["physics", "chemistry", "biology"],
    "history": ["ancient history", "medieval history", "modern history"]
}

difficulty_levels = {
    "easy": (1, 10),
    "medium": (11, 50),
    "hard": (51, 100)
}


def get_question(category, difficulty):
  """Generates a math question based on the chosen category and difficulty."""
  if category == "math":
    operand1 = random.randint(*difficulty_levels[difficulty])
    operand2 = random.randint(*difficulty_levels[difficulty])
    operator = random.choice(["+", "-", "*"])
    question = f"What is {operand1} {operator} {operand2}?"
    answer = eval(f"{operand1} {operator} {operand2}")
    return question, answer
  # Add logic for other categories (science, history) here following a similar pattern

def ask_question(question):
  """Prints the question and gets user input as answer."""
  print(question)
  answer = input("Your answer: ")
  return answer.lower()

def check_answer(answer, correct_answer):
  """Compares user answer with the correct answer and provides feedback."""
  if answer == str(correct_answer):
    print("Correct!")
    return True
  else:
    print(f"Incorrect. The answer is {correct_answer}.")
    return False

def main():
  """Runs the quiz program loop."""
  category = random.choice(list(categories.keys()))
  difficulty = random.choice(list(difficulty_levels.keys()))
  question, answer = get_question(category, difficulty)
  user_answer = ask_question(question)
  is_correct = check_answer(user_answer, answer)

  # Add logic for multiple questions and scorekeeping here

if __name__ == "__main__":
  main()
