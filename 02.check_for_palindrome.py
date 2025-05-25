def is_palindrome(n):
    n = str(n) #meth2 for input by converting numeric value in str
    return n == n[::-1]

# meth1 for input
# expect_string = True
# get_input = lambda:input("Enter value to check whether it's a palindrome or not : ") if expect_string else int(input("Enter value to check whether it's a palindrome or not : "))
# value = str(get_input())

# meth2 for input by 
value = input("Enter the value of n: ")
    
if is_palindrome(value):
    print(f"{value} is a Palindrome")
else:
    print(f"{value} is not a palindrome")

is_palindrome(value)