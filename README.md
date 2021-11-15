# REST API для CRUD операций над объектами Django: ContentType, User, Group, Permission.

_REST API-сервис для CRUD операций над объектами Django_ — это интерфейс, который позволяет создавать, читать, редактировать и удалять стандартные сущности Django в бд. 

# Установка-зависимостей

Весь функионал реализован на платформе m3, доплнительная информация доступна здесь:
1. [Общее описание платформы m3](https://m3-core.readthedocs.io/ru/latest/base.html)
2. [Документация ObjectPack](https://objectpack.readthedocs.io/ru/latest/)
3. [Репозиторий платформы](https://github.com/barsgroup/m3-core)


Для установки зависимостей необходимо в терминале virtuallenv выполнить
	
```
pip3 install -r requirements.txt
./python3 manage.py migrate
```

# Запуск_сервера

Чтобы запустить сервер необходимо выполнить python-файл manage.py

```
./python3 manage.py runserver
```	
