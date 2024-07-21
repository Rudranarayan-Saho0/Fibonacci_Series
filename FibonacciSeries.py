n = int(input("Enter A Number: "))

x = 0
y = 1
z = 0

print(f"fibonacci series of 0 is {x}")
print(f"fibonacci series of 1 is {y}")

i = 1
while i<n:
    z = x+y
    x = y 
    y = z
    i+=1
    print(f"fibonacci series of {i} is {z}")

