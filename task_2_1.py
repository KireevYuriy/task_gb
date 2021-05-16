number = 15
number_2 = 2
number_3 = 3

#Два варианта выяснения типа объеката
#В первом случае выводится тип объекта
print(type(number*number_3))
print(type(number/number_3))
print(type(number//number_2))
print(type(number**number_2))
#Во втором случае выводистя True если тип указан верно
print('Тип данных целочисленный: ',isinstance(number*number_3, int))
print('Тип данных дробный: ',isinstance(number/number_3, float))
print('Тип данных целочисленный: ',isinstance(number//number_2, int))
print('Тип данных целочисленный: ',isinstance(number**number_2, int))
