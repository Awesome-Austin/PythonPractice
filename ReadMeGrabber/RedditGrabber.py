import praw

from definitions import PRAW_CONFIG


def create_reddit_readme(url):
    reddit = praw.Reddit(
        client_id=PRAW_CONFIG['client_id'],
        client_secret=PRAW_CONFIG["client_secret"],
        user_agent=PRAW_CONFIG["user_agent"]
    )

    print(reddit.read_only)


if __name__ == '__main__':
    url = r"https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/"
    create_reddit_readme(url)
