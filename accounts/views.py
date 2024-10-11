from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/dashboard.html')
    # return HttpResponse('<h1>Welcome to Wear & Share!</h1>')