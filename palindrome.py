def palindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
num=input("Enter a number: ")
palindrome(num)78