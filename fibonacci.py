print("Поиск чисел Фибоначчи в диапазоне")

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start >= end:
    print("Ошибка: начало должно быть меньше конца")
else:
    a, b = 0, 1
    result = []
    while a <= end:
        if a >= start:
            result.append(a)
        a, b = b, a + b
    if result:
        print("Числа Фибоначчи в диапазоне:", result)
    else:
        print("В диапазоне нет чисел Фибоначчи")
