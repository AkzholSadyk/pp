def polindrom(word):
    word_reverse=word
    word = word[::-1]
    if word_reverse == word:
        return f"{word_reverse}Yes this word it is polindrom"
    else:
        return f"{word_reverse}No this word it is not polindrom"
word = str(input("enter the word: "))
aa = polindrom(word)
print(aa)


