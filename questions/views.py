
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Data
from django.utils import timezone
from .forms import Queryform
from .serializers import QuestionsSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import UserRateThrottle
from .throttling import UserMinThrottle,UserDayThrottle
import requests

class QuestionsAPIView(ListAPIView):
    queryset = Data.objects.all()
    serializer_class = QuestionsSerializer
    authentication_classes = [SessionAuthentication]
    throttle_classes = [UserRateThrottle,UserMinThrottle,UserDayThrottle]

def indexview(request):
    return render(request,"questions/index.html")

def queryview(request):
    questions_txt = []
    quota = 0
    if request.method == 'POST':
            form = Queryform(request.POST)
            if form.is_valid():
                    form.save()
                    print(Data.objects.all())
                    scope = "https://api.stackexchange.com/2.2/search/advanced"
            
                    params = {
                        "page": request.POST['page'],
                        "pagesize": request.POST['pagesize'],
                        "fromdate": request.POST["fromdate"],
                        "todate": request.POST['todate'],
                        "order": request.POST['order'],
                        "sort": request.POST['sort'],
                        "min": request.POST['min'],
                        "max": request.POST['max'],
                        "q": request.POST['q'],
                        "site": "stackoverflow"
                    }
                    
                    response = requests.get(scope,params=params)
                    print(response.json())
                    questions = response.json()['items']
                    print(response.url)
                    for index, question in enumerate(questions):
                        pretty = "{}. {}\n".format(index + 1, question["title"])
                        print(pretty)
                        questions_txt.append(pretty)
                    
                    quota = "\nYou have {} requests left today.".format(response.json()["quota_remaining"])
                    print("\nYou have {} requests left today.".format(response.json()["quota_remaining"]))


    else:
        form = Queryform()

    context = {'form':form,'question':questions_txt,'quota':quota}
    return render(request, 'questions/query.html', context)




