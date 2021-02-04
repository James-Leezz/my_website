from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request,'my_index_app01/index.html')