#fibonacci series using for loop

a = 0
b = 1

for _ in range(10):
    
    print(f"{a} ",end="")
    a,b = b, a+b
