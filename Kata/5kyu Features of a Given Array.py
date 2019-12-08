"""We are interested in obtaining some different features of given arrays.

For that purpose we will define a class Array that will have the following methods:

num_elements, will give the total of elements of the array.
num_values, will give the total amount of different values of the array.
start_end, will output a list with the first and last element of the array, like [first, last].
range_, will output a list with the minimum and maximum value of the array, like [min_value, max_value].
largest_increas_subseq, will output the largest subsequence (length >= 3) of contiguous elements that are in
increasing order. like [array[i], array[i + 1], array[i + 2], ...., array[i + k]] and
array[i] < array[i + 1] < array[i + 3] < ......< array[i + k]. In case of length less than three, or no increasing pair
at all, this method will output the string: No increasing subsequence
largest_decreas_subseq, will output the largest subsequence (length >= 3) of contiguous elements that are in
decreasing order. like [array[i], array[i + 1], array[i + 2], ...., array[i + k]] and
array[i] > array[i + 1] > array[i + 3] > ......> array[i + k]. In case of length less than three, or no decreasing pair
at all, this method will output the string: "No decreasing subsequence"
__str__, will join the results of all the methods of the class and will output an ordered dictionary,
having the same order as we present the methods.
Let's see an example:

 arr = [345, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
 c = Array(arr)
 c.num_elements() == 13
 c.num_values() == 12
 c.start_end() == [345, 34]
 c.range_() == [12, 345]
 c.largest_increas_subseq() == [12, 45, 47, 49, 55, 90, 104]
 c.largest_decreas_subseq() == "No decreasing subsequence" # [345, 32], [45,12] length less than 3
 c.__str__() == OrderedDict([('1.number of elements', 13), ('2.number of different values', 12), ('3.first and last
 terms', [345, 34]), ('4.range of values', [12, 345]), ('5.increas subseq', [12, 45, 47, 49, 55, 90, 104]),
 ('6.decreas subseq', 'No decreasing subsequence')])
Let's see a case of an array that have both, increasing and decreasing subsequences in contiguous elements.

arr = [345, 288, 250, 215,187, 156, 32, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
c.__str__() == OrderedDict([('1.number of elements', 19), ('2.number of different values', 17), ('3.first and last
terms', [345, 34]), ('4.range of values', [12, 345]), ('5.increas subseq', [12, 45, 47, 49, 55, 90, 104]),
('6.decreas subseq', [345, 288, 250, 215, 187, 156, 32])])
If the result of an increasing or decreasing subsequences is that we have more than one list (of same length, obviously)
, it will be output only the sequence that occurs first in the array.

Assumptions: All the array will have positive integer values, without wrong entries.

Your code will be evaluated mostly by the output of the __str__ method.

The object of the output should be expressed as an ordered dictionary in string format as it is pointed out in your i
nitial solution box.

Enjoy it and happy coding!!"""

from collections import OrderedDict


class Array(object):
    def __init__(self, arr=[]):
        self.arr = arr

    def num_elements(self):
        return len(self.arr)

    def num_values(self):
        return len(set(self.arr))

    def start_end(self):
        return [self.arr[0], self.arr[-1]]

    def range_(self):
        return [min(self.arr), max(self.arr)]

    def largest_increas_subseq(self):
        max_length = 1
        current_length = 1
        sub_array = []

        for i in range(1, len(self.arr)):
            if self.arr[i] > self.arr[i - 1]:
                current_length += 1

                if max_length < current_length:
                    max_length = current_length
                    sub_array = self.arr[i - current_length + 1:i + 1]
            else:
                current_length = 1

        return sub_array if max_length >= 3 else "No increasing subsequence"

    def largest_decreas_subseq(self):
        max_length = 1
        current_length = 1
        sub_array = []

        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i - 1]:
                current_length += 1

                if max_length < current_length:
                    max_length = current_length
                    sub_array = self.arr[i - current_length + 1:i + 1]
            else:
                current_length = 1

        return sub_array if max_length >= 3 else "No decreasing subsequence"

    def __str__(self):
        d = OrderedDict([('1.number of elements', self.num_elements()),
                         ('2.number of different values', self.num_values()),
                         ('3.first and last terms', self.start_end()),
                         ('4.range of values', self.range_()),
                         ('5.increas subseq', self.largest_increas_subseq()),
                         ('6.decreas subseq', self.largest_decreas_subseq())])
        return str(d)
