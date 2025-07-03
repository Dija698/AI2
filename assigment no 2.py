                                              # Assigment no 2
                                              # Question no 01
# Input a sentence from the user
text = input("Enter a sentence: ")

# Split sentence into words
words = text.split()

# List of vowels
vowels = "aeiouAEIOU"

print("Words with vowels:")

# Check each word
for word in words:
    for letter in word:
        if letter in vowels:
            print(word)
            break  # Stop checking once a vowel is found

                                                # Question no 2
# Example list of common nouns (you can expand it)
noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball"]

story = input("Enter a short story: ")

story_words = story.replace(".", "").replace(",", "").split()

found_nouns = []

for word in story_words:
    if word in noun_list:
        found_nouns.append(word)

print("Nouns found in the story:")
for noun in found_nouns:
    print(noun)
                                              # Question no 2b
noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]

story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

found_nouns = []
found_numbers = []

for word in words:
    if word in noun_list:
        found_nouns.append(word)
    elif word.isdigit():
        found_numbers.append(int(word))

found_nouns.append(found_numbers)

print("Final list (nouns with numbers as nested list):")
print(found_nouns)

                                                # Question no 03
noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]


story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

found_nouns = []

for word in words:
    if word in noun_list:
        found_nouns.append(word)

noun_tuple = tuple(found_nouns)

print("Tuple of nouns found in the story:")
print(noun_tuple)

                                             # Question no 3b
noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]

story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

found_nouns = []
found_numbers = []

for word in words:
    if word in noun_list:
        found_nouns.append(word)
    elif word.isdigit():
        found_numbers.append(int(word))

number_tuple = tuple(found_numbers)

found_nouns.append(number_tuple)

final_tuple = tuple(found_nouns)

print("Final tuple (nouns with nested tuple of numbers):")
print(final_tuple)
 

                                                #  Question no 4
noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]

story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

nouns = set()
numbers = set()

for word in words:
    if word in noun_list:
        nouns.add(word)
    elif word.isdigit():
        numbers.add(int(word))

nested_number_set = frozenset(numbers)

nouns.add(nested_number_set)

print("Set of nouns (with numbers as a nested set):")
print(nouns)

                                                  # Question no 05

noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]

story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

nouns_dict = {}
numbers_dict = {}

noun_count = 1
number_count = 1

for word in words:
    if word in noun_list:
        nouns_dict["noun" + str(noun_count)] = word
        noun_count += 1
    elif word.isdigit():
        numbers_dict["number" + str(number_count)] = int(word)
        number_count += 1

nouns_dict["numbers"] = numbers_dict

print("Final dictionary with nouns and nested numbers:")
print(nouns_dict)

                                              # Question no 06

noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]

story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

found_nouns = []

for word in words:
    if word in noun_list:
        found_nouns.append(word)

print("List of nouns found in the story:")
print(found_nouns)
