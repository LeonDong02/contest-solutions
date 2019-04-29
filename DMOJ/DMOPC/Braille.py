a, b, c = '', '', ''
for i in list(input()):
    if i in 'AKUBLVEOZHR':
        a += 'o.'
    elif i in 'CMDNXYFPGQ':
        a += 'oo'
    elif i in 'WISJT':
        a += '.o'
    elif i in ' ':
        a += '..'
    if i in 'AKUCMX ':
        b += '..'
    elif i in 'BLVFPIS':
        b += 'o.'
    elif i in 'WGQHRJT':
        b += 'oo'
    elif i in 'DNEOYZ':
        b += '.o'
    if i in 'ABCDEFGJHIJ ':
        c += '..'
    elif i in 'KLMNOPQRST':
        c += 'o.'
    elif i in 'UVXYZ':
        c += 'oo'
    elif i in 'W':
        c += '.o'
print(a)
print(b)
print(c)
