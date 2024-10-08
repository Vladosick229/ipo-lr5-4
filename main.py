string=input("Введите строку:")

words=string.split()
string1=''
for word in words:
        string1 += word[0]

print("Результат:",string1)