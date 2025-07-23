def expand_word(word):
    
    letters = []

    for i in word:
        if i not in letters:
            letters.append(i)
        else:
            continue
    
    letters.sort()

    return letters

word = input("Input a word here: ")

print(expand_word(word))