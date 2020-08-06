import requests


def create_reddit_readme(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as e:
        raise e

    print(res.text)


if __name__ == '__main__':
    url = r"https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/"
    create_readme(url)
