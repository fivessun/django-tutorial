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

## Formatting
```bash
$ black .
$ isort --profile=google .
```
