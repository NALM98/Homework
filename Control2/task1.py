my_file = open('corp.txt', 'r', encoding = 'UTF-8')
text = my_file.read()
arr = text.split('\n')
my_file.close()

new_file = open('new.txt', 'w', encoding = 'UTF-8')
quant = str(len(arr))
new_file.write(quant)
new_file.close()
