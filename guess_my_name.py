def guess_my_name():
    questions = [
        "Is your name longer than 5 letters? (yes/no) ",
        "Does your name start with a vowel? (yes/no) ",
        "Does your name contain the letter 'a'? (yes/no) ",
        "Is your name common? (yes/no) "
    ]

    possible_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
    answers = []

    for question in questions:
        answer = input(question).strip().lower()
        answers.append(answer)
    
    # Simple logic to guess the name based on answers
    if answers == ["yes", "no", "yes", "yes"]:
        print("I guess your name is Charlie.")
    elif answers == ["no", "yes", "no", "yes"]:
        print("I guess your name is Alice.")
    # Add more conditions based on possible answers
    else:
        print("I couldn't guess your name.")
    
if __name__ == "__main__":
    guess_my_name()
