# Проект по машинному обучению
## Постановка адачи
### Задача

По описанию молока(белки, жиры, углеводы, срок годности и т.д.) и характеристикам человека(рост, вес, возраст, телосложение, индивидуальная непереносимость) определить, полезно ли данное молоко для конкретного человека.

### Формализаия задачи

На вход:
- Характеристики конкретного продукта(молока):
    - с картинки:
        - белки
        - жиры
        - углеводы
        - калорийность
    - ручной ввод - кол-во дней до кона срока годности
- Характеристики конкретного человека:
    - рост
    - вес
    - возраст
    - телосложение(худое, среднее, спортивное, полное)
    - наличие индивидуальной непереносимости молока

На выход: ответ на вопрос "полезен ли данный продукт для данного человека"

## План работы:

- собрать набор данных(dataset), состоящий из описаний продукта(молока) и характеристик людей
- провести предобработку данных, включая числовые и категориальные признаки
- после обработки и нормализации данных разделить датасет на тренировочную и тестовую выборки в соотношении 75:25
- к тестовой выборке применить градиентный метод, тем самым обучив нашу модель на конкретном датасете
- с помощью уже обученной нами моделью получаем предсказание для тестовой выборки
- сравниваем предсказанные результаты тестовой выборки с реальными и убеждаемся в работоспособности модели
- с помощью полученной модели отвечаем на поставленный вопрос 
