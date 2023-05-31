# 9.14
# Дано слово. Вывести на экран его последний символ.

word = 'length'
print(word[5])


# 9.15
# Дано слово. Вывести на экран его "К-тый" символ.

word = input('Input word: ')
k = int(input('Input symbol number: '))
symb = word[k-1]
print(symb)


# 9.16
# Дано слово. Определить, одинаковы ли 2-ой и 4-ый символы в нем.

word = input('Input word: ')
symb2 = word[1]
symb4 = word[3]
if symb2 == symb4:
    print('Yes')
else:
    print('No')


# 9.24
# Из слова "яблоко" путем "вырезок" и "склеек" его букв
# получить слова: "блок" и "око".

word = 'яблоко'

symb2 = word[1]
symb3 = word[2]
symb4 = word[3]
symb5 = word[4]
symb6 = word[5]

print(symb2 + symb3 + symb4 + symb5)
print(symb4 + symb5 + symb6)


# 9.38 (а)
# Дано слово из 12 букв. Поменять местами его трети след образом:
# - 1-ую треть слова разместить на месте третьей, 2-ую на месте
# первой, 3-ю на месте - второй.

word = 'конкатенация'

w1 = word[0:4]
w2 = word[4:8]
w3 = word[8:]

newWord = w2 + w3 + w1
print(newWord)


# 9.41
# Дано название футбольного клуба. Напечатать его на экране "столбиком"

# 1 вариант
word = 'real madrid'
result = 'r' + '\n' + 'e' + '\n' + 'a' + '\n' + 'l' + '\n' + ' ' + '\n' + 'm' + '\n' + 'a' + '\n' + 'd' + '\n' + 'r' + '\n' + 'i' + '\n' + 'd'
print(result)

# 2 вариант
word = 'real madrid'
print('''r
e
a
l

m
a
d
r
i
d''')


# Задача - дана строка 'hello'. Вывести ее наоборот - 'olleh'.

word = 'hello'
print(word[-1] + word[-2] + word[-3] + word[-4] + word[-5])


# 9.59
# Дано предложение. Определить число букв "о" в нем.




