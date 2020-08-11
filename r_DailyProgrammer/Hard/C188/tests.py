import unittest

from r_DailyProgrammer.Hard.C188.test_values import TEST_VALUES
from r_DailyProgrammer.Hard.C188.GridLoops import Grid


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for input, output in TEST_VALUES:
            g = Grid(*input)
            self.assertEqual(max(g.loop_paths.keys()), output)
            print()
            print(g.max_loop())


if __name__ == '__main__':
    unittest.main()
