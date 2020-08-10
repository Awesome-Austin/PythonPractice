#! python3
import datetime
import re
from os import path

from definitions import FILES_DIR, MONTHS_ABBR

def main(input_dates):
    def _mode0(d):
        if d[0] < 100:
            d[0] += 1900
        if d[0] < 50:
            d[0] += 100

        return f'{d[0]}-{d[1]:02d}-{d[2]:02d}'

    def _mode1(d):   # yyyy-mm-dd
        return _mode0([int(d[0]), int(d[2]), int(d[4])])

    def _mode2(d):   # mm/dd/yy
        return _mode0([int(d[4]), int(d[0]), int(d[2])])

    def _mode3(d):   # mm#yy#dd
        return _mode0([int(d[2]), int(d[0]), int(d[4])])

    def _mode4(d):   # dd*mm*yyyy
        return _mode0([int(d[4]), int(d[2]), int(d[0])])

    def _mode5(d):   # (month word) dd, yy OR (month word) dd, yyyy
        return _mode0([int(d[4]), MONTHS_ABBR[d[0].lower()], int(d[2])])

    modes = {
        '-': _mode1,
        '/': _mode2,
        '#': _mode3,
        '*': _mode4,
        ' ': _mode5,
    }

    re_dates = re.compile(r'(.{2,4})([-\s\/\*#])(.{2})([-\s\/\*#,])\s?(.{2,4})')
    matches = re_dates.findall(input_dates)
    return [modes[match[1]](match) for match in matches]


if __name__ == '__main__':
    with open(path.join(FILES_DIR, 'gistfile1.txt')) as f:
        input_dates = f.read()
    ans = main(input_dates)
    # print(input_dates)
    print(list(zip(input_dates.split('\n'), ans))[:10])
