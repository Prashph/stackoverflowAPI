from django import forms
from .models import Data
from datetime import datetime


SORT_CHOICES = ( 
    ("activity", "activity"),
    ("creation", "creation"),  
    )

ORDER_CHOICES = ( 
    ("desc", "desc"), 
    ("asc", "asc"), 
    )

class Queryform(forms.ModelForm):
    page = forms.IntegerField(required = False)
    pagesize= forms.IntegerField(required = False)
    fromdate= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    todate= forms.DateField(initial=datetime.now().strftime("%Y-%m-%d"),required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    order= forms.ChoiceField(choices=ORDER_CHOICES,required = False)
    min= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    max= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    sort= forms.ChoiceField(choices=SORT_CHOICES, required = False)
    q= forms.CharField(empty_value = None,required = False)
    site= "stackoverflow"
    
    class Meta:
        model=Data
        fields="__all__"
        
