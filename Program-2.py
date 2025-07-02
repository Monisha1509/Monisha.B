a = int(input("Enter a number (a): "))

result = []
for i in range(a):
    result.append(2 * i + 1)

print("Output:", ", ".join(map(str, result)))
