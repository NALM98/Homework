# Программа должна обходить всё дерево папок,
# начинающееся с той папки, где она находится, и
# сообщать следующую информацию (далее - по вариантам): 
# 7. в какой папке лежит больше всего файлов.

import os

def file_counter():
    Max = 0
    count = 0
    for root, dirs, files in os.walk('.'):
        for item in root:
            if not item.startswith('.'):
                count = len(files)
                if count > Max:
                    name = os.path.join(root)
                    Max = count
                    count = 0
    print('Максимальное количество файлов -', str(Max) + ',', 'содержится в папке ', name)

file_counter()
