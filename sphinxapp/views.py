from django.shortcuts import render
from sphinxapp.models import Student
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def list(request):
    if request.method=='POST':
        query=request.POST['q']
        query = Student.objects.filter(name__icontains=query)
        if query:
            return render(request, 'list.html', {"list": query})
        else:
            return HttpResponse("<h1>Results Not found!!</h1>")

    else:
        return render(request,'list.html',{'list':list})


