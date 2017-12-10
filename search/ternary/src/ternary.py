
def func(x):
    """
    Рандомная функция, можно брать любую, наверное, 
    главное чтобы впуклая или выпуклая была на диапазоне
    """
    return -1 * pow(x, 2) + 2 * x + 3 


def digits(x):
    """"
    Возвращает число знаков для округления результата
    """
    n = 1
    while x != 1:
        x *= 10
        n += 1
    return n

itterations = 0
def ternary_search_min_recursive(func, left, right, epsillon):
    global itterations
    itterations += 1

    if right - left < epsillon:
        return round((left + right) / 2, digits(epsillon)) # точка минимума с заданной точностью

    # Разбиваем на интервалы [left, a] [a; b] [b; right]
    a = (left * 2 + right) / 3 
    b = (left + right * 2) / 3

    # считаем значения промежуточных точек в функции
    # и в зависимости от этого решаем в каком именно интервале продолжать поиск
    # с каждой иттерацией сужаем область поиска в ~1.5 раза
    if func(a) < func(b):
        return ternary_search_min_recursive(func, left, b, epsillon)
    else:
        return ternary_search_min_recursive(func, a, right, epsillon)

epsillon = 0.0001
min = ternary_search_min_recursive(func, 0, 1, epsillon)

print(min)
print("Itterations: " + str(itterations))