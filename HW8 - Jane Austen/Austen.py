#7. сколько в тексте слов с приставкой un- (слова типа uncle тоже можно считать)
#и какой процент из них имеет длину большую, чем число, введенное пользователем
#(если пользователь ввел число 5, то какой процент слов
#с приставкой un- длиннее 5 символов).

def openfile(name):
    my_file = open(name, encoding = 'UTF-8')
    s = my_file.read()
    name_list = s.split()
    my_file.close()
    return name_list

def un_check(arr = []):
    count = 0
    for item in arr:
        if item.startswith('un') or item.startswith('Un'):
            count += 1
    return count

def length_check(cyph, arr = []):
    count = 0
    for item in arr:
        if len(item) > cyph:
            count += 1
    res = (count / len(arr)) * 100
    return res


def starter():
    file_name = input()
    un_number = un_check(openfile(file_name))
    crit = int(input())
    proc = length_check(crit, openfile(file_name))
    print (un_number, proc)

starter()
    
    
    
    
