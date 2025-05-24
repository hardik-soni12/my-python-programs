def is_palindrome(n):
    return n == n[::-1]

expect_string = True
get_input = lambda:input("Enter value to check whether it's a palindrome or not : ") if expect_string else int(input("Enter value to check whether it's a palindrome or not : "))
value = str(get_input())
    
if is_palindrome(value):
    print(f"{value} is a Palindrome")
else:
    print(f"{value} is not a palindrome")

is_palindrome(value)