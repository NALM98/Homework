from __future__ import print_function
import io

word = ' союз '
with io.open('freq.txt', encoding='utf-8') as file:
    for line in file:
        if word in line1:
            print(line, end='')
