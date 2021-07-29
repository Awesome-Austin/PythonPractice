from math import floor
from pprint import pprint

ROMAN = {
    'I': (1, []),
    'V': (5, ['I']),
    'X': (10, ['I']),
    'L': (50, ['X']),
    'C': (100, ['X']),
    'D': (500, ['C']),
    'M': (1000, ['C'])
}


def roman_numerals(s):
    def _convert_to(s):
        print(s)
        n = ''
        M, s = floor(s / ROMAN['M'][0]), s % ROMAN['M'][0]
        n += 'M' * M

        D, s = floor(s / ROMAN['D'][0]), s % ROMAN['D'][0]
        if D == 4:
            n += 'CD'
        else:
            n += 'D' * D

        C, s = floor(s / ROMAN['C'][0]), s % ROMAN['C'][0]
        if D == 4:
            n += 'CD'
        else:
            n += 'D' * D


        L, s = floor(s / ROMAN['L'][0]), s % ROMAN['L'][0]


        V, s = floor(s / ROMAN['V'][0]), s % ROMAN['V'][0]


        I, s = floor(s / ROMAN['I'][0]), s % ROMAN['I'][0]


        print((M, D, C, L, V, I), s)

        return 0

    def _convert_from(s):
        rn = [ROMAN[n][0] for i, n in enumerate(s)]
        pwr = [(1-(2*int(s[i] in ROMAN[s[(i+1)]][1]))) for i in range(len(s) - 1)] + [1]
        return sum([a * b for a, b in zip(rn, pwr)])

    try:
        ans = _convert_to(int(s))
    except ValueError:
        ans = _convert_from(s)

    return ans


if __name__ == '__main__':
    tests = [
        ('IV', 4),
        ('XXXIV', 34),
        ('CCLXVII', 267),
        ('DCCLXIV', 764),
        ('CMLXXXVII', 987),
        ('MCMLXXXIII', 1983),
        ('MMXIV', 2014),
        ('MMMM', 4000),
        ('MMMMCMXCIX', 4999),
    ]

    for rn, num in tests:
        print(rn, num)
        ans = roman_numerals(num)
        print(ans)
        # break