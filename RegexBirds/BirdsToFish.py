import re

my_file = open('Birds.html', 'r', encoding = 'UTF-8')
text = my_file.read()
my_file.close()
text = re.sub(u'<.*?>&a-zA-Z', u'', text, flags = re.U)
arr = text.split()

var1 = re.compile('Птиц(а|ы|у|е|ам|ах|ами)')
var2 = re.compile('[^\w]птиц(а|ы|у|е|ам|ах|ами)')
var3 = re.compile('Птицей')
var4 = re.compile('[^\w]птицей')

s = ''
for item in arr:
    if re.search(var1, item):
        item = re.sub(u'Птиц', u'Рыб', item, flags = re.U)
    elif re.search(var2, item):
        item = re.sub(u'птиц', u'рыб', item, flags = re.U)
    elif re.search(var3, item):
        item = re.sub(u'Птицей', u'Рыбой', item, flags = re.U)
    elif re.search(var4, item):
        item = re.sub(u'птицей', u'рыбой', item, flags = re.U)

for item in arr:
    s += ' ' + item + ' '
    
new_file = open('Forms.txt', 'w', encoding = 'UTF-8')
new_file.write(s)
