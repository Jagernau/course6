# Курсовая работа по Django API

Backend для интернет магазина. Фронтэнд предоставлен в учебных целях.
1. Скопировать репозиторий `git clone https://github.com/Jagernau/course6`
2. Изменить данные для создания БД в `course6/market_postgres/docker-compose.yaml` в отделе db/environment под себя. 
3. Изменить данные для подключения к БД в `course6/skymarket/skymarket/settings.py`:
* Узнать HOST, postgres можно вообще где угодно запускать. В compose создаётся Сеть skymarket, узнать точнее: `sudo docker network ls`, а потом проинспектировать её `inspect`
4. Создать env, войти в песочницу, установить зависимости из course6/requirements.txt:
* Скорее всего psycopg2 при установке выдаст ошибку, установить postgres.
5. Запустить фронт nginx и бд в `course6/market_postgres/` через `sudo docker-compose up`
6. Мигрировать таблицы `course6/skymarket/manage.py migrate`
7. Запустить проект `course6/skymarket/manage.py runserver`
