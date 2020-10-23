import math
print("Усынин Ю.А. ИУ5-55Б")

def func():
    try:
        a, b, c = map(int, input('Введите через пробел значения коэффициентов a, b, c:').split())
        if a==0:
            flag = input("Коффициент 'a' не должен быть равен нулю! Попробовать заново? [да/нет]")
            if flag == "да":
                func()
            else:
                exit(0)
    except Exception:
        flag=input("Данные введены неверно! Попробовать заново? [да/нет]")
        if flag=="да":
            func()
        else:
            exit(0)
    else:
        return a,b,c

a,b,c = func()

d = b**2 - (4*a*c)
if d<0:
    print("Данное уравнение не имеет действительных корней!")
    exit(0)
else:
    y1=(-b-math.sqrt(d))/(2*a)
    y2=(-b+math.sqrt(d))/(2*a)

    if y1<0 and y2<0:
        print("Данное уравнение не имеет действительных корней!")
        exit(0)
    elif y1>=0 and y2<0:
        x1=math.sqrt(y1)
        x2=-x1
        print("x1 = ",x1,"x2 = ",x2)
        exit(0)
    elif y1<0 and y2>=0:
        x1=math.sqrt(y2)
        x2=-x1
        print("x1 = ",x1,"x2 = ",x2)
        exit(0)
    elif y1 >= 0 and y2 >= 0:
        x1 = math.sqrt(y1)
        x2 = -x1
        x3 = math.sqrt(y2)
        x4 = -x3
        print("x1 = ", x1, "x2 = ", x2,"x3 = ", x3, "x4 = ", x4)
        exit(0)

