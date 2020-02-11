from django.shortcuts import render
from app.forms import CarSearchForm
from app.models import Car
from django.views.generic import FormView
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
filter_cars = Car.objects.all()

def CheckInput(brand = '', model = '', since = '', until = ''):
    if since:
        try:
            since = int(since)
        except ValueError:
            raise
    if until:
        try:
            until = int(until)
        except ValueError:
            raise
    if brand and model and since and until:
       return Car.objects.filter(Q(brand_name=brand) & Q(car_model=model) 
       & Q(release_year__gte=since) & Q(last_year__lte=until))
    if model and since and until:
        return Car.objects.filter(Q(car_model=model) & Q(release_year__gte=since) & Q(last_year__lte=until))
    if brand and since and until:
        return Car.objects.filter(Q(brand_name=brand) & Q(release_year__gte=since) & Q(last_year__lte=until))
    if brand and model and until:
        return Car.objects.filter(Q(brand_name=brand) & Q(car_model=model) & Q(last_year__lte=until))
    if brand and model and since:
        return Car.objects.filter(Q(brand_name=brand) & Q(car_model=model) & Q(release_year__gte=since))
    if brand and model:
        return Car.objects.filter(Q(brand_name=brand) & Q(car_model=model))
    if brand and since:
        return Car.objects.filter(Q(brand_name=brand) & Q(release_year__gte=since))
    if brand and until:
        return Car.objects.filter(Q(brand_name=brand) & Q(last_year__lte=until))
    if model and since:
        return Car.objects.filter(Q(car_model=model) & Q(release_year__gte=since))   
    if model and until:
        return Car.objects.filter(Q(car_model=model) & Q(last_year__lte=until))
    if since and until:
        return Car.objects.filter(Q(release_year__gte=since) & Q(last_year__lte=until))
    if brand or model or since or until:
        if not since:
            return Car.objects.filter(Q(brand_name=brand) | Q(car_model=model) | Q(last_year__lte=until))
        else:
           return Car.objects.filter(Q(release_year__gte=since))
    else:
        return Car.objects.all()
    

def FilterCar(request):
    filter_brand_name = request.GET['brand_name']
    filter_car_model = request.GET['car_model']
    filter_release_year = request.GET['release_year']
    filter_last_year = request.GET['last_year']
    print("brand_{}; model_{}; since_{}; until_{}.".format(filter_brand_name, filter_car_model, filter_release_year, filter_last_year))
    global filter_cars
    filter_cars = CheckInput(filter_brand_name, filter_car_model, filter_release_year, filter_last_year)
    return redirect('/')

def SearchResult(request):
    template = loader.get_template('index.html')
    form = CarSearchForm()
    result = []
    for car in filter_cars:
        result.append(car)
    return HttpResponse(template.render({'form': form, 'result': result}, request))

