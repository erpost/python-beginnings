def tf_quiz(question, answer):
    response = input("(T/F) " + question + ": ")
    if response.lower() == answer.lower():
        tf_quiz = "correct"
        return tf_quiz
    else:
        tf_quiz = "incorrect"
        return tf_quiz


quiz_eval = tf_quiz("Octopuses have three hearts", "T")
print("your answer is", quiz_eval)