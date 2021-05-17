ls = [57.8, 46.54, 97, 101.5, 15.3, 77.847, 94.02, 50, 2]
string = ''
for elem in ls:

    if int(elem//1) < 10:
        string += f'0{elem:.2f} '
    else:
        string += f'{elem:.2f} '
print(string)

