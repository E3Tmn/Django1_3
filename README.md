# Сайт экскурсионных услуг
На сайте отображается карта, на которой указаны местоположения компаний, предоставляющих экскурсионные услуги, а так же информация об этих компаниях.
https://nikitapin.pythonanywhere.com/
## Запуск
Python3.9 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
1. Скачайте проект
2. Установите зависимости командой `pip install -r requirements.txt`
3. Перед запуском проекта примените миграции командой `python3 manage.py migrate`
4. Запустите сайт командой `python3 manage.py runserver`
5. Для доступа к базе данных создайте супер-пользователя командой `python3 manage.py createsuperuser`
## Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл .env рядом с manage.py и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступны 3 переменные:
- `DEBUG` — [дебаг-режим](https://docs.djangoproject.com/en/5.0/ref/settings/#debug). Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — [секретный ключ проекта](https://docs.djangoproject.com/en/5.0/topics/signing/#protecting-secret-key-and-secret-key-fallbacks)
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts).
## Добавление локации на карту
```
python manage.py load_place http://адрес/файла.json
```
[Пример файла JSON.](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Генератор%20Маркса%20или%20«Катушка%20Тесла».json)
