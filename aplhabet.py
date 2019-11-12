text1 = input("Choose a or b: ")
alphabet = ('abcdefghijklmnopqrstuvwxyzабвгдеєжзиїйклмнопрстуфхцчшщьюя')
if text1 == "a":
    test_str = input("Please enter word: ")

    all_freq = {}

    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    print("Your word :\n "
          + str(all_freq))
if text1 == "b":
    import re

    text = input("Please enter your word: ")
    shortword = re.compile(r'\W*\b\w{2}\b')
    print(shortword.sub('', text))