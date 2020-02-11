from django import forms  
from app.models import Car  
  
  
class CarSearchForm(forms.ModelForm):  
    class Meta:  
        model = Car  
        fields = ['brand_name', 'car_model', 'release_year', 'last_year']