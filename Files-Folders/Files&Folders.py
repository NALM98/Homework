# Программа должна просмотреть все папки и файлы,
# находящиеся в одной папке с ней, и сообщить следующую информацию:
# Сколько найдено папок, название которых содержит и кириллические,
# и латинские символы.
# Кроме этого, программа должна выводить на экран названия всех файлов или
# папок, которые она нашла, без повторов (это задание на 9 и 10).

import os

def openfile(file):
    with open(file, encoding = 'UTF-8') as my_file:
        text = my_file.read()
    return set(text.split())

def check(name):
    flag1, flag2 = False, False
    for item in name:
        if item in openfile('cyr.txt'):
            flag1 = True
        elif item in openfile('lat.txt'):
            flag2 = True
    if flag1 and flag2:
        return True
    else:
        return False

names = set()
count = 0
for f in os.listdir():
    if check(f):
        names.add(f)
        if os.path.isdir(f):
            count += 1
print('Найдено таких папок: ', count, '\n' 
      'Файлы и папки такого рода: ', *names)

