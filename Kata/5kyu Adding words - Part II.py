class Arith:

    def __init__(self, first_number):
        self.first_number = first_number
        self.transform_set = {
                        'teens': ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                                  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                                  'eighteen', 'nineteen', 'twenty'],

                        'tens': ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                                 'ninety'],

                        'hundreds': ['hundred', 'thousand']
                     }

    def _words_into_digit(self, string):
        words = string.split()

        if len(words) == 5:
            number = self.transform_set['teens'].index(words[0]) * 100 + self.transform_set['tens'].index(words[3]) *\
                      10 + self.transform_set['teens'].index(words[4])

        elif len(words) == 4:
            if words[3] in self.transform_set['teens']:
                number = self.transform_set['teens'].index(words[0]) * 100 + self.transform_set['teens'].index(words[3])
            else:
                number = self.transform_set['teens'].index(words[0]) * 100 +\
                         self.transform_set['tens'].index(words[3]) * 10
        elif len(words) == 2:
            if words[1] == 'hundred':
                number = self.transform_set['teens'].index(words[0]) * 100

            elif words[0] in self.transform_set['tens']:
                number = self.transform_set['tens'].index(words[0]) * 10 + self.transform_set['teens'].index(words[1])

            else:
                number = 1000

        else:
            if words[0] in self.transform_set['tens']:
                number = self.transform_set['tens'].index(words[0]) * 10
            else:
                number = self.transform_set['teens'].index(words[0])

        return number

    def _digits_into_words(self, number):
        if number in range(21):
            word = self.transform_set['teens'][number]

        elif number in range(21,100):
            word = self.transform_set['tens'][int(str(number)[0])] + ' ' +\
                   self.transform_set['teens'][int(str(number)[1])]

        elif number in range(100,1000):
            if not number % 100:
                word = self.transform_set['teens'][int(str(number)[0])] + ' ' + 'hundred'

            elif int(str(number)[1]) in range(2):
                word = self.transform_set['teens'][int(str(number)[0])] + ' ' + 'hundred' + ' ' + 'and' + ' ' +\
                       self.transform_set['teens'][int(str(number)[1:])]

            elif int(str(number)[1]) in range(2,10) and int(str(number)[2]) == 0:
                word = self.transform_set['teens'][int(str(number)[0])] + ' ' + 'hundred' + ' ' + 'and' + ' ' + \
                       self.transform_set['tens'][int(str(number)[1])]

            else:
                word = self.transform_set['teens'][int(str(number)[0])] + ' ' + 'hundred' + ' ' + 'and' + ' ' + \
                       self.transform_set['tens'][int(str(number)[1])] + ' ' + \
                       self.transform_set['teens'][int(str(number)[2])]

        else:
            word = 'one thousand'

        return word

    def add(self, second_word):
        digit_result = self._words_into_digit(self.first_number) + self._words_into_digit(second_word)
        return self._digits_into_words(digit_result)

