from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def calci(requests):
    field1=int(requests.GET['field1'])
    field2=int(requests.GET['field2'])
    operation=requests.GET['optradio']
    result=0
    if operation=='+':
        result=field1+field2
    elif operation=='-':
        result=field1-field2
    elif operation=='*':
        result=field1*field2
    elif operation=='/':
        result=field1/field2
    return render(requests,'calci/calci.html',{'result':result})
def home(requests):
    return render(requests,'calci/home.html')