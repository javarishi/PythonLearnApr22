'''
Loop - Iterative programming logic

while condition:
    block of code executes till condition is true
    condition modifier
'''

# Addition for 1 to 10
count = 1
total = 0
while count <= 10:
    total = total + count
    print("Count ", count)
    count += 1 # condition modifier

print("Total", total)