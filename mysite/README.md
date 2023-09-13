# mysite : django tutorial project

## Migration

```bash
$ python manage.py makemigrations # 변경사항 확인
$ python manage.py migrate # 적용
```

## Run Local Server
```bash
$ python manage.py runserver
# If you want to change port (default: 8080)
$ python manage.py runserver {{ port_number:8080 }}
```

## Create SuperUser
```bash
$ python manage.py createsuperuser
> Username: {{ username:admin }}
> Email address: {{ email:admin@example.com }}
> Password: **********
> Password (again): *********
> Superuser created successfully.
```

## Formatting
```bash
$ black .
$ isort --profile=google .
```
