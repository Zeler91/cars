import csv, sys, os

project_path = sys.path[0] + '\cars'

sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
import datetime

django.setup()

from app.models import Car

data = csv.reader(open(sys.path[0] + '\csv.csv'), delimiter = ';')

for row in data:
    car = Car()
    car.brand_name = row[0]
    car.car_model = row[1]
    car.release_year = row[2]
    car.name = "{} - {}".format(row[0], row[1])
    try:
        car.last_year = int(row[3])
    except ValueError:
        car.last_year = datetime.datetime.today().year  
    car.save()