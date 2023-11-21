"""
CS 122 Fall 2023 Lab 7 Word Check
Author: Oliver Boorstein
Credit:
Description: Check if inputted word is in word list from words_alpha.txt.
"""


while True:
    word = input("Enter a search word (blank to exit): ").strip()
    if word == "":
        break
    
    
    word_list = open("CS122F23\wk7\words_alpha.txt")

    count = 0
    word_found = False

    for line in word_list:
        count += 1
        
        if word.lower() == line.strip().lower():
            print(f"Word {word} found")
            word_found = True
            break
        
    if not word_found:
        print(f"Word {word} not found") 
        
    word_list.close()
    # print(count)



# print(word_list.readline(), end='')
# print(word_list.readline(), end='')
# print(word_list.readline(), end='')
