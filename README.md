# Cars_Filter
 
1. склонировать этот репозиторий;
2. перейти в папку с ним;
3. создать виртуальное окружение python -m venv venv;
4. активировать его;
5. установить зависимости pip install -r requirements.txt;
6. находясь в папке /cars в командной стоке набрать python manage.py runserver;
7. В отдельной командной строке импортировать данные по автомобилям из csv-файла: python import.py (может занять несколько минут).
8. Настройка nginx:
listen 80;
server_name 130.193.38.144;

location / {
 proxy_pass http://127.0.0.1:8000;
}
