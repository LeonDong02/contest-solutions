from collections import deque


key = deque(['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'])
keyOriginal = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
inversion, triadType = 0, ''
notes = deque([input() for i in range(3)])
while triadType == '':
    key = deque(keyOriginal)
    key.rotate(-(key.index(notes[0])))
    diff1 = key.index(notes[1]) - key.index(notes[0])
    diff2 = key.index(notes[2]) - key.index(notes[1])
    if diff1 == 4 and diff2 == 3:
        triadType = 'major'
    elif diff1 == 3 and diff2 == 4:
        triadType = 'minor'
    elif diff1 == 3 and diff2 == 3:
        triadType = 'diminished'
    elif diff1 == 4 and diff2 == 4:
        triadType = 'augmented'
    else:
        inversion += 1
        notes.rotate(1)
print(notes[0])
print(triadType)
if inversion == 0: print('root position')
if inversion == 1: print('first inversion')
if inversion == 2: print('second inversion')