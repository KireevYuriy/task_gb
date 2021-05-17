ls = [57.8, 46.54, 97, 101.5, 15.3, 77.84, 94.02, 50.4, 2]

string = ''
for elem in ls:

    price = str(elem).split('.')
    if len(price) == 1:
        price.append('00')
    string += f'{price[0]} руб {price[1]} коп '
print(string)






