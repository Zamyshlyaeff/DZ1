# Задача 2: Найдите сумму цифр трехзначного числа.
a=input('Введите трёхзначное число: ')
d=0
for i in a:
    d+=int(i)
print(d)
