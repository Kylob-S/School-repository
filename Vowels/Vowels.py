def count_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 } #Dictionary filled with vowels

    vowel_count = 0
    for char in string: #loop that adds 1 for every vowel
        if char.lower() in vowels:
            vowels[char.lower()] += 1
            vowel_count += 1

    return vowel_count, vowels

text = input("Enter a String: ")#User input

total, vowel_counts = count_vowels(text) #Grabs the total amount of vowels(caps or not) adds them.
print(f"Total number of vowels: {total}")#Prints the full amount of vowels entered
for vowel, count in vowel_counts.items():
    print(f"{vowel} = {count}")
