class Arith:
    transform_set = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                     'nineteen', 'twenty']

    def __init__(self, first_word):
        self.first_word = first_word

    def add(self, second_word):
        return self.transform_set[self.transform_set.index(self.first_word) + self.transform_set.index(second_word)]


