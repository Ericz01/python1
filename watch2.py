import re

#<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

def main():
    print(parse(input('HTML: ')))
def parse(s):
    if matches := re.search(r'<iframe(.)*(http(s)?:\/\/(www\.)?youtube\.com\/embed\/)([a-zA-Z0-9]+)(.)*><\/iframe>', s):
            return 'https://youtu.be/' + matches.group(5)
            
if __name__ == "__main__":
    main()