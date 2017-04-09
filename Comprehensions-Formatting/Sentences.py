# 7. Для каждого предложения найти слова, которые встретились
#в предложении больше, чем 1 раз,
#и распечатать табличку с выравниванием по центру, в которой сказано,
#сколько раз они встретились. Например, для предложения
#"А это веселая птица-синица, которая часто ворует пшеницу,
#которая в темном чулане хранится в доме, который построил Джек."
#распечатать:
#которая           2 
#в            2
import re

my_file = open('rask.txt', encoding = 'UTF-8')
text = my_file.read()
my_file.close()

regex = '[!?]'
new_text = re.sub(regex, '.', text)

sent = [item.split() for item in new_text.split('.')]

for words in sent:
    unique = set()
    for word in words:
        word.strip('. , : -')
        if words.count(word) > 1 and word not in unique:
            unique.add(word)
            print('{:^10} {:^10}'.format(word, words.count(word)))
