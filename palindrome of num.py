def palindrome(num):
    if num == num[::-1]:
        print("f{num} is a palindrome")
    else:
        print("f{num} is not a palindrome")
num=input("Enter a number: ")
print(palindrome(num))
