# -*- coding: utf-8 -*-
"""ML_project3.ipynb

Automatically generated by Colaboratory.

"""

from google.colab import files  # из библиотеки google.colab импортируем класс files
import pandas as pd             # для вывода данных
from sklearn.preprocessing import StandardScaler                          # импортируем класс StandardScaler для нормализации данных

uploaded = files.upload()       # загружаем файл с данными с компьютера

train = pd.read_csv('/content/milk_dataset_1.csv')      # применим функцию read_csv() и посмотрим на первые три записи файла train.csv
train.head(3)

train.info()

"""Поработаем с категориальными переменными (categorical variable).
  
Т.к. категории телосложений выражены числами 1(худощавое), 2(среднее), 3(спортивное), 4(полное), то модель воспримет их в качестве количественных переменных, а не категориальных, поэтопу применим one-hot encoding. В библиотеке Pandas есть метод .get_dummies(), который как раз и выполнит необходимые преобразования.
"""

physique = pd.get_dummies(train['Physique'], drop_first = True)       # разбиваем телосложение на категории "1", "2", "3" и "4", затем отбрасываем столбец "1", т.к. он избыточен

train = pd.concat([train, physique], axis = 1)              # проводим конкатенацию нашего основного набора данных с полученным ранее набором категорий телосложения
train

train.drop(['Physique'], axis = 1, inplace = True)      # избавляемся от уже ненужного столбца 'Physique'
train.head(3)                                           # показываем получившийся набор данных

"""Оставшиеся переменные представляют собой либо количественные, либо категориальные признаки, выражены через 0 и 1.

Для избежания ситуации, в которой модель неоправданно придает большее значение признаку с большей числовой характеристикой, получая соответственно ошибочный результат, проведем нормализацию данных и приведем количественные переменные к одному масштабу.
"""

scaler = StandardScaler()                                                 # создадим объект класса StandardScaler
cols_to_scale = ['Proteins (g)', 'Fats (g)', 'Carbohydrates (g)',
                 'Calories', 'Days until the end of the shelf life',
                 'Weight (kg)', 'Height (cm)', 'Age']                     # выберем те столбцы, которые мы хотим масштабировать
scaler.fit(train[cols_to_scale])                                          # рассчитаем среднее арифметическое и СКО для масштабирования данных
train[cols_to_scale] = scaler.transform(train[cols_to_scale])             # нормализуем данные

train                                                                     # посмотрим на результат

train.columns = train.columns.map(str)               # приведем все названия колонок к строковому формату

X_all = train.drop('Usefulness of the product for humans', axis = 1)         # поместим в X_all все кроме столбца 'Usefulness of the product for humans', т.е. нашего target
y_all = train['Usefulness of the product for humans']                        # столбец 'Usefulness of the product for humans' станет нашей целевой переменной

X_all.head(3)

X=X_all.values        # для большего удобства приведем наши данные к типу numpy.ndarray
y=y_all.values
X

"""# Обучение модели

В итоге мы привели данные к необходимому виду, далее можем разбивать нашу выборку на тренировочную и тестовую части и проризводить обучение модели методом градиентного бустинга.
"""

import numpy as np                                              # для математических вычислений
import sklearn                                                  # воспользуемся библиотекой, в которой уже разработан метод градиентного бустинга
from sklearn.model_selection import train_test_split            # для разделения наших данных на тестовую и тренировочную выборки
from sklearn.ensemble import GradientBoostingRegressor          # метод градиентного бустинга

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)       # формирование наших выборок

np.random.seed(2)
sklearn_model = GradientBoostingRegressor()
sklearn_model.fit(X_train, y_train)                             # применение градиентного бустинга и обучение модели на тренировочной выборке

y_pred_train = sklearn_model.predict(X_train)                   # модель обученав => посмотрим, как хорошо она предскажет данные, на которых обучалась

import matplotlib.pyplot as plt                                 # для отрисовки графиков и более наглядного представления полученных результатов

def plot_two_ys(y_pred, y_test, y_pred_name, y_test_name):
  plt.figure(figsize=(15, 10))
  plt.plot(y_pred, label=y_pred_name)
  plt.plot(y_test, label=y_test_name)
  plt.legend(fontsize=20)
  plt.xlabel('Observation number', fontsize=20)
  plt.ylabel('Usefulness of the product for humans', fontsize=20)
  plt.show()

plot_two_ys(y_pred_train,  y_train, "y_pred_train", "y_train")

"""Видим, что обучение модели прошло успешно и она себя отлично показывает на тренировочной выборке. Далее посмотрим на результаты тестовой выборки."""

y_pred_test = sklearn_model.predict(X_test)
plot_two_ys(y_pred_test,  y_test, "y_pred_test", "y_test")

"""Видим, что модель на тестовой выборке показывает себя чуть хуже, но все равно работает достаточно точно."""