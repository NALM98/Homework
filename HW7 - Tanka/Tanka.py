# Текст должен представлять собой танка, то есть стихотворение на русском языке
# из пяти строк без рифмы, при этом длина первой строки должна быть 5 слогов,
# второй строки - 7 слогов, третьей строки - 5 слогов,
# четвёртая и пятая строка - по 7 слогов
# Количество предложений в таком тексте может быть любым
import random

def subj():
    subj_file = open('nouns.txt', encoding = 'UTF-8')
    s = subj_file.read()
    subj_list = s.split()
    return random.choice(subj_list)
    subj_file.close

def act():
    act_file = open('activities.txt', encoding = 'UTF-8')
    s = act_file.read()
    act_list = s.split()
    return random.choice(act_list)
    act_file.close()

def sylls_counter(word):
    vowels = open('vowels.txt', encoding = 'UTF-8')
    s = vowels.read()
    mark = s.split()
    vowels.close()
    count = 0
    for item in word:
        if item in mark:
            count += 1
    return count

def obj():
    obj_file = open('objects.txt', encoding = 'UTF-8')
    s = obj_file.read()
    obj_list = s.split()
    return random.choice(obj_list)
    obj_file.close()

def puncmark():
    punc_file = open('punctuation.txt', encoding = 'UTF-8')
    s = punc_file.read()
    punc_list = s.split()
    return random.choice(punc_list)
    punc_file.close()
    
def composer():
    line = (subj().capitalize() + ' ' + act() + ' ' + obj()) + puncmark()
    return line

def check7(w7):
    if sylls_counter(w7) == 7:
        return 1
    else:
        return 0

def check5(w5):
    if sylls_counter(w5) == 5:
        return 1
    else:
        return 0
    
def final_tanka():
    for i in range(5):
        a = composer()
        if i in [0, 2]:
            c = 0
            while c != 1:
                a = composer()
                c = check5(a)
            print(a)
        else:
            d = 0
            while d != 1:
                a = composer()
                d = check7(a)
            print(a)

final_tanka()
