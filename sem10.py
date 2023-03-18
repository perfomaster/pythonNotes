# Библиотека для работы с табличными данными
import pandas as pd
# Библиотека для вычислений линейной алгебры
import numpy as np
# Библиотеки для визуализации
import seaborn as sns
import matplotlib.pyplot as plt


# Задача №1: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# вывод сгенерированной таблицы
print(data[:5])
data.head()
# создаем список из таблицы
data_list = data.values.tolist()
print(data_list[:5])
# создаем переменные из уникальных записей списка
uniq = []
for var in data_list:
    flag = True # флаг, по совпадению имени в списке уникальных переменных
    for check in uniq:
        if var == check:
            flag = False
    if flag == True: # если таких записей нет
        uniq.append(var)
# выводим уникальные записи
print(uniq)
# выводим hot-форму
df_dict = {'whoAmI':lst}
for i in uniq:
    df_dict[str(i[0])] = []
print(df_dict)
# заполняем столбцы, с уникальными переменными
for i in range(len(lst)):
    for n in uniq:
        if lst[i] == str(n[0]):
            df_dict[str(n[0])].append(1)
        else:
            df_dict[str(n[0])].append(0)
print(df_dict)
new_df = pd.DataFrame(df_dict)
new_df.head()


