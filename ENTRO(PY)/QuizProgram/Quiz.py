quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },

    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },

    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },

    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },

    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisboa"
    },

    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        score += 1
        print('Your score is : ' + str(score))
        print('Correct! Congratulations!')
        print("")
        print("")
    else:
        print('ITS WRONG, YOU PUSSY')
        print('THE FUCKING ANSWER IS : ' + value['answer'])
        print('YOUR BITCH SCORE IS: ' + str(score))
        print("")
        print("")
