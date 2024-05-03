[Описание дипломного проекта](../README.md)

Запуск: 

1. создать вирт. окружение
2. установить зависимости
```bash
pip install -r orders/requirements.txt
```
3. задать значения в файле `orders/.env`
4. создать базу данных 
```bash
createdb -U postgres <your_db_name>
```
5. произвести миграции 
```bash
python orders/manage.py migrate
```
для silk:
```bash
python orders/manage.py collectstatic
```
6. запустить redis
```bash
redis-server
redis-cli
```
7. запустить celery 
```bash
celery -A orders.orders worker --loglevel=info
```
8. запустить приложение 
```bash 
python orders/manage.py runserver
```
9. посылать запросы на сервер можно, например, через [postman-collection](../postman_collection.json)
