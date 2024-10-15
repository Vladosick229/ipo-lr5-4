string=input("Введите строку:")#ввод строки

words=string.split()#инициализация переменной words
string1=''#инициализация переменной string
for word in words:#цикл for
        string1 += word[0]#инициализация превых букв

print("Результат:",string1)#вывод результата
