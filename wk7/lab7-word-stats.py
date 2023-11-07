"""
CS 122 Fall 2023 Lab 7 Word Stats
Author: Oliver Boorstein
Credit:
Description: Display cool info about words_alpha.txt
"""
def reverse(str):
    """
    Reverses given string

    Loops through str to concatenate it to reversed_string

    Args:
        str (str): string inputted on function call

    Returns:
        the variable reversed_string
    """
    reversed_string = ""
    for i in str:
        reversed_string = i + reversed_string
    return(reversed_string)


def letter_calc(letter, file):
    word_list = open(file)
    count = 0
    amount = 0
    percentage = 0

    for line in word_list:
        count += 1
        if line[0] == letter:
            
            amount += 1

    word_list.close()

    percentage = round(amount / count * 100, 2)
    return amount, percentage

# Tally and display word count
word_list = open("wk7\words_alpha.txt")
count = 0

for line in word_list:
    count += 1

print(f"Count: {count}")
word_list.close()

# Find and display longest word
word_list = open("wk7\words_alpha.txt")
longest_word = ""

for line in word_list:
    if len(line.strip()) > len(longest_word):
        longest_word = line.strip()

print(f"Longest word is {longest_word} ({len(longest_word)})")
word_list.close()

# Find and display shortest word
word_list = open("wk7\words_alpha.txt")

shortest_word = longest_word

for line in word_list:
    if len(line.strip()) < len(shortest_word):
        shortest_word = line.strip()

print(f"Shortest word is {shortest_word} ({len(shortest_word)})")
word_list.close()

# Find Palindromes
word_list = open("wk7\words_alpha.txt")
palindrome_count = 0

for line in word_list:
    if line.strip() == reverse(line.strip()):
        palindrome_count += 1
print(f"Palindromes: {palindrome_count} ({round(palindrome_count/count*100, 2)}%)")
word_list.close()

# Find all words that start with letters and their percents
print("First letter counts")
alpha_words_count = 0
for c in "abcdefghijklmnopqrstuvwxyz":
    print(f"{c.upper()}: {letter_calc(c, 'wk7/words_alpha.txt')[0]} ({letter_calc(c, 'wk7/words_alpha.txt')[1]}%)")
    alpha_words_count += letter_calc(c, 'wk7/words_alpha.txt')[0]

 
other_count = alpha_words_count - count
other_percent = round(other_count/count * 100, 2)
print(f"Other: {other_count} ({other_percent}%)")

