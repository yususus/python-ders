a = 5
while a < 16:
    print(a)
    a += 1
    if a == 8:
        continue
    if a == 12:
        break
    print(a)

else:
    print("a artık 16 ya da daha büyük")