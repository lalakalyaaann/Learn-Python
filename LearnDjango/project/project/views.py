from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import UserForm

def aboutus(request):
    return render(request,"aboutus.html")

def courses(request):
    return HttpResponse("This is the page for course")

def coursedetails(request,courseid):
    return HttpResponse(courseid)

def Homepage(request):
     data ={
        'title':'Home Page ',
        'bdata':'This is body paragraph',
        'clist':['PHP','Java','Django'],
        'number':[10,20,30,40,50,55],
        'studentdetails':[
            {'name':'Kalyan','phone':9801234567},
            {'name':'Ishan','phone':9876543210}
        ],
         'ages': 
         [12, 17, 18, 20, 15, 25, 16, 30],
         }
     return render(request,"index.html",data)



def userform(request):
    finalans = 0
    fn = UserForm()          
    data = {'form': fn}

    if request.method == "POST":
        try:
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2

            url = "/about-us/?output={}".format(finalans)
            return redirect (url)

        except (TypeError, ValueError):
         
            data['error'] = "Please enter valid numbers for both fields."

    return render(request, "userform.html", data)


def submitform(request):
         return HttpResponse(request)

