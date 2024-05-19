strr = str(input())
words = strr.split()
reversed_words = []
for word in words:
    rev_word = word[::-1]
    reversed_words.append(rev_word)
revers_string = ' '.join(reversed_words)
print( revers_string)
