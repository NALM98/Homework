from __future__ import print_function
import io

word = ' жен '
with io.open('freq.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            stop = ' '
            i = 0
            tail = len(line)
            ipm = 0
            while line[i] != stop:
                print(line[i], end = ' ')
                i += 1
