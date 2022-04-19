
count = 1
total = 0

while count <= 10:
    print(count)
    if count == 5:
        print("Breaking")
        break
    total = total + count
    count += 1

print("Loop is Broken at count ", count)


count = 1
total = 0
# condition modifier should be executed before continue statement
while count <= 10:
    if count == 5:
        print("Skipping..")
        count += 1
        continue
    print(count)
    total = total + count
    count += 1

