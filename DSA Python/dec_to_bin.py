def dtb(num):
    result = []
    while num != 1:
        whole = num//2
        rest = num%2
        result.append(rest)
    return f"{result}"


#The above code converts from decimal to bianry
a = dtb(1341)
   