string = input('File name: ').lower().strip().split('.', 1)[1]
splits = len(string)
if splits != 3:
    print('application/octet-stream')
    exit
else:
    if string == 'gif':
        print('image/gif')
    elif string == 'jpg' or string == 'jpeg':
        print('image/jpeg')
    elif string == 'png':
        print('image/png')
    elif string == 'pdf':
        print('application/pdf')
    elif string == 'txt':
        print('text/plain')
    elif string == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')

