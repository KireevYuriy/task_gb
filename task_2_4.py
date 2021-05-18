list_price = [57.8, 46.54, 97, 101.5, 15.3, 77.84, 94.2, 50.4, 5.00, 2]
revers_list_price = [57.8, 46.54, 97, 101.5, 15.3, 77.84, 94.2, 50.4, 5.00, 2]

string = ''

# Задание *. Сортировка элементов списка происходит в цикле. В результате сам список не изменяется.
for elem in sorted(list_price):

    price = str(elem).split('.')

    if len(price) == 1:
        price.append('00')
    elif price[1] == '0':
        price[1] = f'0{price[1]}'

    if int(price[0]) // 10 == 0:
        price[0] = f'0{price[0]}'
    elif int(price[1]) // 10 == 0 and price[1] != '00':
        price[1] = f'0{price[1]}'

    if elem != list_price[-1]:
        string += f'{price[0]} руб {price[1]} коп, '
    else:
        string += f'{price[0]} руб {price[1]} коп.'

print(string)
print('Входний список цен: ',list_price)

# Задание **. Новый список отсортированный по убыванию.
string = ''
revers_list_price.sort(reverse = True)
for elem in revers_list_price:

    price = str(elem).split('.')

    if len(price) == 1:
        price.append('00')
    elif price[1] == '0':
        price[1] = f'0{price[1]}'

    if int(price[0]) // 10 == 0:
        price[0] = f'0{price[0]}'
    elif int(price[1]) // 10 == 0 and price[1] != '00':
        price[1] = f'0{price[1]}'

    if elem != revers_list_price[-1]:
        string += f'{price[0]} руб {price[1]} коп, '
    else:
        string += f'{price[0]} руб {price[1]} коп.'


print(string)
print('Входной, отсортированный по убыванию список: ',revers_list_price)
# Задание ***. Вывод 5 цен самых дорогих товаров.
check = 0
for num in range(0,len(string),1):
    if string[num] == 'п':
        check += 1
        if check <= 5:
            lenght = num+1
            
print('Список 5 самых дорогих цен: ',string[:lenght])












