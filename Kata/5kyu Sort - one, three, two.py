"""Hey You !

Sort these integers for me ...

By name ...

Do it now !

Input

Range is 0-999
There may be duplicates
The array may be empty"""


n2w = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
       10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
       17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
       60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 200: 'two hundred',
       300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred',
       800: 'eight hundred', 900: 'nine hundred', 0: 'zero'
       }


def _digits_into_words(number):
    word = ''

    try:
        word = n2w[number]
    except KeyError:
        try:
            word = ' '.join([n2w[number - number % 10], n2w[number % 10]])
        except KeyError:
            try:
                word = ' '.join([n2w[number - number % 100], n2w[number % 100]])
            except KeyError:
                try:
                    word = ' '.join([n2w[number - number % 100], n2w[number % 100 - number % 10], n2w[number % 10]])
                except KeyError:
                    print('Number out of range')

    return word


def sort_by_name(arr):
    res = sorted([(_digits_into_words(number), number) for number in arr])
    return [t[1] for t in res]

