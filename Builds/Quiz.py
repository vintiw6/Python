questions = {
    "Q.1 How many planets are there?": 8,
    "Q.2 How many bones does an average human have?": 206,
    "Q.3 What is the largest ocean on Earth?": "Pacific Ocean",
    "Q.4 How many days are there in a leap year?": 366
}

for question, answer in questions.items():
  print(question)
  user = input("Enter your answer: ")
  if str(user).lower() == str(answer).lower(): 
    print("Correct! Just for fun, imagine you've won $100!")
  else:
    print("Incorrect. The answer is", answer)

print("Thanks for playing!")
