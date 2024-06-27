#  Аттестационное задание "Онлайн платформа торговой сети электроники"
## Задание
Создайте веб-приложение с API-интерфейсом и админ-панелью.

Создайте базу данных, используя миграции Django.

## Требования к реализации:

Необходимо реализовать модель сети по продаже электроники.
Сеть должна представлять собой иерархическую структуру из трех уровней:

###  завод;

###  розничная сеть;

###  индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.

###  Каждое звено сети должно обладать следующими элементами:

Название.

Контактная информация (email, страна, город, улица, номер дома).

Продукты (название, модель, дата выхода продукта на рынок).

Поставщик (предыдущий по иерархии объект сети).

Задолженность перед поставщиком в денежном выражении с точностью до копеек.

Время создания (заполняется автоматически при создании).

###  Сделать вывод в админ-панели созданных объектов.

На странице объекта сети добавить:

ссылку на «Поставщика»;

фильтр по названию города;

admin action, очищающий задолженность перед поставщиком у выбранных объектов.

###  Используя DRF, создать набор представлений:

CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).

Добавить возможность фильтрации объектов по определенной стране.

Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.


# Инструкция по установке:

В файле .env.default необходимо внести данные в поле `SECRET_KEY` , значения переменных окружения, заданные по умолчанию, важно изменить перед запуском проекта. 

Для установки зависимостей необходимо активировать виртуальное окружение командой  `venv\Scripts\activate`  и выполнить  `pip install -r requirements.txt`  .

Для создания базы данных необходимо в консоли подключиться к postgres  командой `psql -U <ваш логин>`, далее ввести пароль и выполнить `create database <ваше название базы данных>;`

После подтверждения создания базы выйти из postgres командой `\q`

Затем применить миграции командой `python manage.py migrate`  и запустить сервер `python manage.py runserver`  .

Для доступа к административной странице используется команда создания суперпользователя `python manage.py csu`  (по умолчанию заданы логин 'admin@test.ru' и пароль '12345')

### Краткое описание:

Просмотреть документацию к проектам можно по ссылкам `/redoc/` или `/swagger/` 

Авторизация пользователя реализована с помощью simplejwt, при создании нового пользователя необходимо указать его email и пароль. Дальнейшее редактирование профиля будет доступно после присвоения ему актикного статуса(в админ-панели)

