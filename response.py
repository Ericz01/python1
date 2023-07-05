from validator_collection import validators

def main():
    print(validate(input('Email: ')))

def validate(s):
    try:
        if matches := validators.email(s):
            return 'Valid'
    except:
        return 'Invalid'
if __name__ == "__main__":
    main()