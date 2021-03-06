# Солвер для капчи "[Humans Not Invited](http://www.humansnotinvited.com/)"

Всем лежать, у нас машинное обучение!

Здесь лежит простейший бот для прохождения данной капчи.
Принцип его работы крайне прост:


## Первая часть бота

1. Делаем over 1000 запросов капчи
2. Вытаскиваем имя категории для которой необходимо выбрать картинки
3. Скачиваем все картинки из капчи
4. Считаем md5 хэш от каждой картинки
5. Собираем словарь частот встречамости картинки для каждой категории
6. Сохраняем словарь на диск в каком-нибудь JSON'e

Спустя 1000 запросов, получаем неплохой ~~датасет~~ словарь частот, по которому можно понять, принадлежит ли данная картинка, к данной категории.

## Вторая часть бота (собственно сам бот)

1. Читаем наш словарь с диска
2. С помощью Selenium открываем браузер и переходим на сайт с капчей
3. Парсим имя запрашиваемой категории и скачиваем картинки
4. Считаем для каждой картинки хэш и смотрим, как часто для запрашиваемой категории встречалась картинка с таким то хэшем в словаре
5. Если частота больше 10 (выбрано наобум), то это хорошая картинка, кликаем по ней
6. После того как прокликаем все нужные картинки, нажимаем Verify и радуемся

P.S. 

Для работы данного бота нужно скачать драйвер для вашего браузера и положить в той же директории что и скрипт. Например, у меня Google Chrome, поэтому драйвер качаю [отсюда](https://chromedriver.chromium.org/).

Так же нужно использовать соответствующий метод загрузки этого драйвера. Это строка 23 в файле solver.py