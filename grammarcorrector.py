from spellchecker import SpellChecker

correct_my_spelling = SpellChecker()
new_word = input("what word comes to mind ? ")

if new_word in correct_my_spelling:
    print("Awesome")
else:
    correct_word = correct_my_spelling.correction(new_word)
    print("Correct Spelling is ", correct_word)

