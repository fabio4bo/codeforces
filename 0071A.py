"""
71/A - Way Too Long Words - Difficulty 800
"""

n = int(input())

for i in range(n):
    word = input()

    if len(word) > 10:
        abrev = "" + word[0] + str(len(word) - 2) + word[len(word) - 1]
        print(abrev)
    else:
        print(word)
