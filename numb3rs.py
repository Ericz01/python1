import re

def main():
    print(validate(input('IPv4 Address: ')))

def validate(ip):
    if matches := re.search(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', ip):
        first, second, third, fourth = ip.split('.')
        if int(first) < 256 and int(second) < 256 and int(third) < 256 and int(fourth) < 256:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    main()