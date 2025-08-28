secret_word = "endeavor"
correct_letter = ""
new_name = ""
i = 0
while True:
    i += 1
    question = input("Enter a letter that you believe is in the secret word: ")
    if len(question) > 1:
        print("The maximun of letters is 1")
        continue
    if question in secret_word:
        correct_letter += question
    new_name = ""
    for censured_word in secret_word:
        if censured_word in correct_letter:
            new_name += censured_word
        else:
            new_name += "*"
    print(new_name)

    if new_name == secret_word:
        print("correct word,congratulations!! ")
        print(f"you used {i} tries")
        print(f"the secret word is : {secret_word}")
        break
