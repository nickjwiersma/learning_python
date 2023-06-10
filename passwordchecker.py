# selfmade password checker python 3 that registers the name of the people trying to access and have accessed the document code
username = input('Please state your name: ')
password = input('Please state the correct password.')
password_length = len('supersecret')
code_document = 'notreallysecure'

# create loop to ask password until correct

for item in password:
    if password == 'supersecret':
        print (f'Hi {username} the password is correct! {code_document} is the code to the document.')
        with open('.triedtoaccess.txt', 'a') as file:
            file.write(f'{username} Has the code to access the document. \n')
        break

    else:
        print(f'password incorrect, please try again. Password length is {password_length} characters long.')
        password = input('Please state the correct password.')
        with open('.triedtoaccess.txt', 'a') as file:
            file.write(f'{username} unsuccessfully tried to access the document with the password: {password}. \n')
 