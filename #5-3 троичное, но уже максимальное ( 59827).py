c=set()
for n in range (1, 100):
    i = n
    s = ''
    while i > 0:
        s += str(i%3)
        i //= 3
    s = s[::-1]
    if n % 3 == 0:
        s += s[-2:]
    if n % 3 != 0:
        k = 5 * (n % 3)
        while k > 0:
            p = ''
            p += str(k%3)
            k //= 3
            s += p[::-1]
    d = int(s, 3)
    if d < 173:
        c.add(d)
        print(max(c))
