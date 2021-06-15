# django-and-postgres-on-docker
template



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
