input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result_str = ''

for elem in input_list:
    idx = input_list.index
    check = 0

    for symbol in elem:
        for number_str in range(0,9,1):
            number_str = str(number_str)
            if number_str == symbol:
                check += 1
            number_str = int(number_str)
            number_str += 1
    if check == 1:
        if len(elem) == 1:
            result_str += f'"{int(elem):02}" '
        else:
            result_str += f'"{elem[0]}'
            result_str += f'{int(elem[1]):02}" '
    elif check > 1:
        result_str += f'"{elem}" '
    else:
        result_str += f'{elem} '

print(result_str)





