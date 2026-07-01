from django.http import HttpResponse
from django.shortcuts import render 
def aboutus(request):
    return HttpResponse("Hello Guys!")

def courses(request):
    return HttpResponse("This is the page for course")

def coursedetails(request,courseid):
    return HttpResponse(courseid)

def Homepage(request):
     data ={
        'title':'Home Page ',
        'bdata':'This is body paragraph'
          }
     return render(request,"index.html",data)
