import re

t_file = open('Finnish.html', encoding = 'UTF-8')
lines = t_file.read()
t_file.close()

clearing = re.compile('<[/]?[a-z]*>')
lines = re.sub(u'<.*?>', u'', lines, flags = re.U)
p1 = re.compile('ISO 639-3\D', re.IGNORECASE)
p2 = re.compile('\n[a-z]{3}', re.IGNORECASE)
m1 = p1.search(lines)
m2 = p2.search(lines[m1.end():len(lines)])
print(m1.group(), m2.group())
