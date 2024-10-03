# 1. Функция с параметрами по умолчанию:
# Создаем функцию print_params(a = 1, b = 'строка', c = True),
# которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True)
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # Вывод значений параметров
print('******')

print ('Вызов функции print_params с разным количеством аргументов')
print_params(5, 'ququ', True)
print_params(5, 'ququ')
print_params(a=1, b=2, c=3)
print_params(a=1, b=2)
print_params(b=2, c=3)
print_params(a=1, c=3)
print_params(a=1)
print_params(b=2)
print_params(c=3)
print_params()
print('******')

print ('Работа вызовов print_params(b = 25) и print_params(c = [1,2,3])')
print_params(b=25)
print_params(c=[1, 2, 3])
print('******')

print ('Список')
values_list = [5, 'ququ', True]
print ('Словарь с тремя ключами')
values_dict = {'a': 'else', 'b': False, 'c': 0}
print ('Передача values_list и values_dict в функцию print_params')
print_params(*values_list)
print_params(**values_dict)
print('******')

print('Распаковка')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
