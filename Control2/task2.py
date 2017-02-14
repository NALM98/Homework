import re

my_file = open('corp.txt', encoding = 'UTF-8')
text = my_file.read()
arr = text.split()
my_file.close()

a = []
b = []
un = []
count = 0

for i in range(len(arr)):
    if 'type' in arr[i] and 'lemma' in arr[i + 1]:
        item = arr[i]
        left_num = item.find('"')
        right_num = item.rfind('"')
        a.append(item[left_num + 1 : right_num])

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if a[i] not in un:
        un.append(a[i])
    b.append(count)
    count = 0

my_dictionary = dict(zip(un, b))
print(my_dictionary)

new_file = open(new.txt, 'w', encoding = 'UTF-8')
new_file.write(my_dictionary)
new_file.close()
