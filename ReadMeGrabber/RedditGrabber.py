import re
import os

import praw
import pandas as pd

from definitions import PRAW_CONFIG, DAILYPROGRAMER_POSTS_DIR, ROOT_DIR


def create_reddit_files(post):
    def _create_readme():
        with open(os.path.join(post_dir, 'README.md'), 'w', encoding="utf-8") as f:
            f.write(f'{post.selftext}\n\nTaken from Reddit: {post.url}')

    def _create_main():
        with open(os.path.join(post_dir, 'main.py'), 'w') as f:
            f.write("""#! python3

def main():
    pass
""")

    def _create_init():
        with open(os.path.join(post_dir, '__init__.py'), 'w') as f:
            f.write(f"""#! python3

from r_DailyProgrammer.{match[3]}.{match[1]}{match[2]}.main import main

""")

    def _create_tests():
        test_dir = os.path.join(post_dir, 'unittests')
        try:
            os.mkdir(test_dir)
        except FileExistsError:
            pass

        with open(os.path.join(test_dir, 'test_values.py'), 'w') as f:
            f.write("""#! python3
from collections import namedtuple

TEST_VALUE = namedtuple('TEST_VALUE', 'INPUT OUTPUT')

#TEST_VALUES = [
#    TEST_VALUE(, )
#]
""")

            with open(os.path.join(test_dir, 'unittest.py'), 'w') as f:
                f.write(f"""#! python3
import unittest

from r_DailyProgrammer.{match[3]}.{match[1]}{match[2]}.unittests.test_values import TEST_VALUES 


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
""")

    re_post = re.compile('\[(\d{4}-\d{2}-\d{2})\] (\w)\w* #(\d*) \[(.*)\]\s?(.*)?')
    try:
        match = re_post.findall(post.title)[0]
    except IndexError as e:
        if post.title == "Open Discussion Threads":
            return True
        else:
            print(f'\t{str(e)}')
            return False

    post_dir = os.path.join(ROOT_DIR, 'r_DailyProgrammer', match[3], f'{match[1]}{match[2]}')
    os.makedirs(post_dir, exist_ok=True)

    tasks = [
        _create_readme,
        _create_main,
        _create_init,
        _create_tests
    ]

    for task in tasks:
        try:
            task()
        except Exception as e:
            raise e

    return True

def get_dailyprogrammer_posts(limit):
    previous_posts = pd.read_csv(DAILYPROGRAMER_POSTS_DIR)

    reddit = praw.Reddit(
        client_id=PRAW_CONFIG['client_id'],
        client_secret=PRAW_CONFIG["client_secret"],
        user_agent=PRAW_CONFIG["user_agent"]
    )

    sub = reddit.subreddit('dailyprogrammer')
    for submission in sub.new(limit=limit):
        if not (previous_posts['id'].eq(submission.id)).any():
            print(submission.title)
            if create_reddit_files(submission):
                d = {
                    'title': submission.title,
                    'id': submission.id,
                    'url': submission.url
                }
                previous_posts = previous_posts.append(d, ignore_index=True)

    previous_posts = previous_posts.set_index('id')
    previous_posts.to_csv(DAILYPROGRAMER_POSTS_DIR)


if __name__ == '__main__':
    get_dailyprogrammer_posts(limit=5000)

