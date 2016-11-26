#7. Каждый раз обрезаем два крайних символа и выводим строку на экран в таком виде

given_word = input('Введите, пожалуйста, любое слово: ')
while len(given_word) > 0:
    print(given_word)
    given_word = given_word[1:len(given_word) - 1]
