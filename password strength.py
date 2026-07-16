import string
password=input('enter a password with at least 6 char and at least one special character: ')
str=len(password)
if str<6:
    print('password is weak')
elif str>=6 and str<=10:
    if str>=6 and any(char in string.punctuation for char in password):
        print('password is moderate')
else:
     print('password is strong')