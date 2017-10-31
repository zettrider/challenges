from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as f:
        RSS_CONTENT = f.read()
    RSS_TAGS_DASH = TAG_HTML.findall(RSS_CONTENT.lower())
    RSS_TAGS_CLEAN = []
    for item in RSS_TAGS_DASH:
        RSS_TAGS_CLEAN.append(item.replace("-", " "))
    return RSS_TAGS_CLEAN


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    CLEAN_LIST = []
    TAG_PRODUCT_LIST = []
    TAG_PRODUCT_DICT = {}
    for i in range (0, TOP_NUMBER - 1):
        CLEAN_LIST.append(top_tags[i][0])
    TAG_PRODUCT_LIST=list(product(CLEAN_LIST, CLEAN_LIST))
    for i in range (0, len(TAG_PRODUCT_LIST)):
        seq = SequenceMatcher(None, TAG_PRODUCT_LIST[i][0], TAG_PRODUCT_LIST[i][1])
        d = seq.ratio()
        if d > SIMILAR:
            TAG_PRODUCT_DICT[TAG_PRODUCT_LIST[i][0]] = TAG_PRODUCT_LIST[i][1]
    return TAG_PRODUCT_DICT
 


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
