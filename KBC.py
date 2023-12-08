import random
#Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

questions = ["what is the capital of india?", "who is the prime minister of india?", "who is the president of india?", "Which of the following is observed as Sports Day every year?", "World Health Day is observed on?"]

answers = ["delhi", "narendra modi", "draupadi murmu", "29 august", "7 april"]

flag = 0
random_choice = random.choice(questions)

print(random_choice)
answer_from_user = str(input("Enter the answer:"))
ans = answer_from_user.lower()

if ans in answers:
    print("Correct Answer")
    flag = flag + 1
else:
    print("Wrong Answer")
    flag = 0

