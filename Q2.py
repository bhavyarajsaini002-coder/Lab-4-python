password = ""

while password != 's3cr3t!P@ssw0rd':
    password = input('Enter password: ')
    if password == 's3cr3t!P@ssw0rd':
        print('welcome')
    else:
        print('wrong password')