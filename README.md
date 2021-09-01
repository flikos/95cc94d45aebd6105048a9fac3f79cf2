[Описание задания](https://github.com/flikos/95cc94d45aebd6105048a9fac3f79cf2/blob/main/Тестовое%20задание.%20Начинающий%20Python%20разработчик..pdf)

# django-and-postgres-on-docker
template based on  
https://webdevblog.ru/kak-ispolzovat-django-postgresql-i-docker/


Собираем  
```$ docker-compose build```

Запускаем  
```$ docker-compose up -d```

Смотрим логи, если не работает  
```$ docker-compose logs -f```

Останавливаем с удалением контейнеров  
```$ docker-compose down -v```



Если очистка базы не нужна, комментируем  
flush  
migrate  
строчки в entrypoint.sh

После этого при необходимости можно вручную чистить  
```$ docker-compose exec web python manage.py flush --no-input```  
```$ docker-compose exec web python manage.py migrate```

Создание администратора  
```$ docker-compose exec web python3 manage.py createsuperuser```


Запуск Celery  
~~ docker-compose exec web celery -A alytics worker ~~

Реализован в докере

