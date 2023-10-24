'''
checkout the link for description of this program:
https://cs50.harvard.edu/python/2022/psets/7/watch/



'''

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if html_url := re.search (r"^\<iframe.+\>\<\/iframe\>", s):
        if matches := re.match(r"^.+https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+).+$", s):
            url="http://youtu.be/"
            return url + matches.group(1)
        else:
            return None
    else:
        sys.exit("HTML format not correct")


...


if __name__ == "__main__":
    main()


# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>           