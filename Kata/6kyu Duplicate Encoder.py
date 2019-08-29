'''The goal of this exercise is to convert a string to a new string where each character in the new string is
"(" if that character appears only once in the original string, or ")" if that character appears more than once in the
original string. Ignore capitalization when determining if a character is a duplicate.

Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
'''


def duplicate_encode(word):
    result = []
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            result.append(')')
        elif word_lower.count(letter) == 1:
            result.append('(')
        print(letter, word_lower.count(letter), result)
    return "".join(result)