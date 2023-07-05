import re

#<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

def main():
    print(parse(input('HTML: ')))
def parse(s):
    if re.search(r'<iframe(.)*><\/iframe>', s):
        match2 = re.search(r'(http(s)?:\/\/(www\.)?youtube\.com\/embed\/)([a-zA-Z0-9]+)', s)
        if match2:
            return 'https://youtu.be/' + match2.group(4)
            
if __name__ == "__main__":
    main()