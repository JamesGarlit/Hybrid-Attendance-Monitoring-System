from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'webportal/dashboard.html')
def leave_management(request):
    return render(request, 'webportal/leave_management.html')
def login(request):
    return render(request, 'webportal/login.html')
# Create your views here.
