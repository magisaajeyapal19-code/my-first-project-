def palindrome(str):
    if str==str[::-1]:
       print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")
str=input('enter a word :')
print(palindrome(str))
    
    
    
