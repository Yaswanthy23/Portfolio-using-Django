from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request,'index.html')
def projects(request):
     return render(request,'main.html')
def info(request):
     return render(request,'info.html')