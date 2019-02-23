scale = input().split()
if sorted(scale) == scale:
    print('ascending')
if sorted(scale, reverse=True) == scale:
    print('descending')
elif sorted(scale, reverse=True) != scale and sorted(scale) != scale:
    print('mixed')