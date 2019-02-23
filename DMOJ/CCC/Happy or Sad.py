text, counter = input(), 0
counter -= text.count(':-(')
counter += text.count(':-)')
if counter > 0: print('happy')
if counter < 0: print('sad')
if counter == 0 and text.count(':-)') == 0: print('none')
elif counter == 0: print('unsure')
