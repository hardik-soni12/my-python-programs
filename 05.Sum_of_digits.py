# using while loop
n = 1343

meth1 = 0
while n > 0:
    meth1 += n % 10
    n = n // 10

print(f"Sum of digits = {meth1}")


# Using a for loop with str()
n2 = 1234

meth2 = 0
for digit in str(n2):
    meth2 += int(digit)

print(f"Sum of digits = {meth2}")