'''Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.'''

from string import ascii_lowercase


def high(x):
    def f_score(word):
        score = 0
        for letter in word:
            score += (ascii_lowercase.index(letter) + 1)
        return score

    def f_scores(x):
        scores = []
        for word in x.split():
            scores.append((f_score(word), word))
        return scores

    return sorted(f_scores(x), reverse=True)[0][1]