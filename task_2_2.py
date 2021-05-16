input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# (Задание 2.Вариант с дополнительным списком)
# Новый список для добавления в него отформатированных элементов
result_array = []

# (Задание 3) Переменная для записи итогового результата в строку, без использования дополнительного списка
result_str = ''

for elem in input_list:

    # Переменная счетчик, для проврки цифр в элементах списка
    check = 0
    for symbol in elem:
        for number_str in range(0,9,1):
            number_str = str(number_str)
            if number_str == symbol:
                check += 1
            number_str = int(number_str)

    #  Проверка на колличество цифр в элементах списка(число разрядов)
    if check == 1:
        # Проверка на дополнительный знак "+/-" перед числом
        if len(elem) == 1:
            # Добавление форматированного элемента в итоговую строку, не меняя входной список
            result_str += f'"{int(elem):02}" '

            # Добавление форматированного элемента в новый список, не меняя входной список
            result_array.append('"')
            result_array.append(f'{int(elem):02}')
            result_array.append('"')
        else:
            # Добавление форматированного элемента в итоговую строку, не меняя входной список
            result_str += f'"{elem[0]}'
            result_str += f'{int(elem[1]):02}" '

            # Добавление форматированного элемента в новый список, не меняя входной список
            result_array.append('"')
            result_array.append(f'{elem[0]}{int(elem[1]):02}')
            result_array.append('"')
    # Проверка на колличество цифр в элементах списка(число разрядов)
    elif check > 1:
        # Добавление форматированного элемента в итоговую строку, не меняя входной список
        result_str += f'"{elem}" '

        # Добавление форматированного элемента в новый список, не меняя входной список
        result_array.append('"')
        result_array.append(f'{elem}')
        result_array.append('"')
    # Добавление не числовых элементов массива
    else:
        result_str += f'{elem} '
        result_array.append(elem)

print(result_array)

print(result_str)

# print(list(result_str.split(sep = ' ')))






