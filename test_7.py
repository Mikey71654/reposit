from functools import reduce
#1  Создать один список с городами два варианта (второй в одну строку)
my_list = [['Екатеринбург', 'Москва'], ['Санкт-Петербург', 'Норильск'], ['Пермь', 'Астрахань']]
list0 = []
for i in my_list:
    list0 += i
print(list0)
print(sum(my_list, []))





#2  Найти сумму чисел по диагонали (второй в одну строку)
data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]
print(sum(value[key] for key, value in enumerate(data)))
chislo = 0
for key, value in enumerate(data):
    chislo += value[key]
print(chislo)



#3  Найти средний возраст данных людей (второй в одну строку)
people = {1: {'name': 'Oleg', 'age': '29', 'sex': 'Male'},
          2: {'name': 'Kate', 'age': '21', 'sex': 'Female'},
          3: {'name': 'Liza', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Pavel', 'age': '36', 'sex': 'Male'}}
print(sum([int(value['age']) for value in people.values()]) / len(people))
c = 0
for key, value in people.items():
    c += int(value['age'])
print(c/len(people))



#4  Написать функцию, которая может принимать много значений(типа *args и **kwargs) и находила среднее значение стоимости квартир)
district_1 = {'flat_1': 10500, 'flat_2': 11000}
district_2 = {'flat_3': 15000}
district_3 = {'flat_4': 6500, 'flat_5': 7000, 'flat_6': 6000}
# def func(**kwargs):






#5  Найти все визиты в Россию, второй вариант через функцию filter
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit7': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
for d in geo_logs:
    if 'Россия' in list(d.values())[0]:
        print(d)



print(list(filter(lambda d: 'Россия' in list(d.values())[0], geo_logs)))


#6  Создать список, состоящий из средних значений, второй вариант через функцию map
prices_by_categories = [[100, 200, 400, 600], [200, 500], [100, 200, 100, 100], [800, 900]]
list1 = []
for list in prices_by_categories:
    list1.append(sum(list)/len(list))
print(list1)



#7  Создать словарь {'2018-01-01': {'yandex': {'cpc': 100}}}, два варианта второой использовать функцию reduce
some_list = ['2018-01-01', 'yandex', 'cpc', 100]
print(reduce(lambda key, value: {value: key}, reversed(some_list)))
