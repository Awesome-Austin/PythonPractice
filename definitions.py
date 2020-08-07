import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(ROOT_DIR, 'configs')

with open(os.path.join(CONFIGS_DIR, 'praw.json')) as f:
    PRAW_CONFIG = json.load(f)
