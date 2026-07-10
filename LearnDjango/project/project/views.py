from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect

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

from django.shortcuts import render

def calculator(request):
    data = {
        "n1": "",
        "n2": "",
        "c": ""
    }
    try:
        if request.method == "POST":
            # Get values from form
            data["n1"] = request.POST.get("num1")
            data["n2"] = request.POST.get("num2")
            opr = request.POST.get("opr")
            # Convert to numbers
            n1 = float(data["n1"])
            n2 = float(data["n2"])
            # Perform calculation
            if opr == "+":
                data["c"] = n1 + n2
            elif opr == "-":
                data["c"] = n1 - n2
            elif opr == "*":
                data["c"] = n1 * n2
            elif opr == "/":
                if n2 != 0:
                    data["c"] = n1 / n2
                else:
                    data["c"] = "Cannot divide by zero."
    except ValueError:
        data["c"] = "Invalid DataType. Please enter int/float value."
    return render(request, "calculator.html", data)


def oddeven(request):
    data={
        "n":'',
        "c":'',
    }
    if request.method =="POST":
        data["n"]=eval(request.POST.get('number'))
        if data["n"] %2==0:
           data["c"]="Number is even"
        else :
            data["c"]="Number is odd "


    return render(request,"oddeven.html",data)