# Program to count frequency of words and characters

text = input("Enter a text string: ")

# Convert text to lowercase
text = text.lower()

# Word frequency
words = text.split()
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Character frequency
character_frequency = {}

for char in text:
    if char != " ":
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1

print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(word, ":", count)

print("\nCharacter Frequency:")
for char, count in character_frequency.items():
    print(char, ":", count)
