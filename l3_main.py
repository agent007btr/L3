F=63
a=input("Введите ваше имя ")
print(a)
b=int(input("сколько вам лет "))
print(b)
if b<F:
    c=F-b
    print("до пенсии осталось", c)
else:
     print("уже пенсия")