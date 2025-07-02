a = int(input("Enter a number (a): "))

count = a if a % 2 != 0 else a - 1

result = []
for i in range(count):
    result.append(2 * i + 1)

print("Output:", ", ".join(map(str, result)))
