
def tri_recursion(count):
    if count > 0:
        result = count + tri_recursion(count - 1)
        print(count, result)
    else:
        result = 0
    return result

total = tri_recursion(5)
print("Recursion total", total)