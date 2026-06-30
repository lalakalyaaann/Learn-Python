from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("Hello Guys!")

def courses(request):
    return HttpResponse("This is the page for course")

def coursedetails(request,courseid):
    return HttpResponse(courseid)