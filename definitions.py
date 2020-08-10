import os
import json

MONTHS_ABBR = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12
}


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(ROOT_DIR, 'configs')
FILES_DIR = os.path.join(ROOT_DIR, 'files')
ENABLE1_DIR = os.path.join(FILES_DIR, 'enable1.txt')

DAILYPROGRAMER_POSTS_DIR = os.path.join(FILES_DIR, 'dailyprogrammerposts.csv')

with open(os.path.join(CONFIGS_DIR, 'praw.json')) as f:
    PRAW_CONFIG = json.load(f)

with open(ENABLE1_DIR) as f:
    ENABLE1 = f.read().splitlines()
