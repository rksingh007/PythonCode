vowels = ['a','e','i','o','u']
found = []
word = input("privide a word to search for vowel: ")
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
print(found)
