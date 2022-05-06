def dtb(num):
    result = []
    while num != 1:
        whole = num//2
        rest = num%2
        result.append(rest)
    return result



a = dtb(1341)
print(a)    