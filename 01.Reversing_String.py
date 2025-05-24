name = "Hardik"

# 1) reversing string using reversed() with join():

r1 = "".join(reversed(name))
print(f"Reversed name using Join() = {r1}\n ")


# 2) reversing string using slicing:

r2 = name[::-1]
print(f"Reversed Name using Slicing = {r2}\n")


# 3) reversing string using loop:

r3 = ""
for char in name:
    r3 = char + r3
print(f"Reversing String using loop = {r3}")