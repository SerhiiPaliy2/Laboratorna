text1 = input("Choose a or b: ")
alphabet = ('abcdefghijklmnopqrstuvwxyzабвгдеєжзиїйклмнопрстуфхцчшщьюя1234567890')
if text1 == "a":
    test_str = input("Please enter word: ")

    all_freq = {}

    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    print("Your word :\n " + str(all_freq))

if text1 == "b":
    text = input("Please enter your word: ")

    all_freq = {}

for i in text:
    if i in all_freq:
         all_freq[i] += 1
    else:
        all_freq[i] = 1

print("Your word :\n " + str(all_freq))
import re

shortword = re.compile(r'\W*\b\w{2}\b')
print(shortword.sub('', text))