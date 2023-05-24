class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        roman_int = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'],
                     [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'],
                     [5, 'V'], [4, 'IV'], [1, 'I']]

        for num_roman_pair in roman_int:
            while num >= num_roman_pair[0]:
                roman += num_roman_pair[1]
                num -= num_roman_pair[0]

        return roman
