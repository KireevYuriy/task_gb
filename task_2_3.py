input_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee_name in input_list:
     employee_name = employee_name.lower()
     employee_name = employee_name.split(sep = ' ')
     print (f'Привет, {employee_name[-1].title()}!')
