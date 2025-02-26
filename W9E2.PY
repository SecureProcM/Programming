
# you start with an empty list
words = []

# ask the user to input 5 words and each word
for i in range(5):

    word = input(f"Enter word# {i+1}: ")

    words.append(word)




# add the word done to the list
words.append("done")

print(words)



# Create a new list and copy words containing the letter "o" to this new list

new_list = []

for word in words:

    if "o" in word:

        print(f"Copying word {word} to the new list")

        new_list.append(word)



# Then Print the new list

print("New list:", new_list)

