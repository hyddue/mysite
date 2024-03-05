from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")


#파싱은 뭐고 패싱은 뭔지 제대로?