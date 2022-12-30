word = "shailesh"

wrong_words = []

for i in range(5):
    spelling = input("Type a test spelling : ")
    wrong_words.append(spelling)

check_word = input("Type the word to auto correct")
print("you typed : ",check_word)
if check_word==word:
    print("No need to autocorrect")
else:
    if check_word in wrong_words:
        print("Autocorrected : ", word)

