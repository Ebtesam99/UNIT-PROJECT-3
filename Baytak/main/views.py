from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact




def homePage(request : HttpRequest):

    return render(request ,"main/homePage.html")
def not_found_view(request:HttpRequest):
    return render(request,"main/not_found.html")

def contact(request : HttpRequest ):
    try:
        user = request.user
        if request.method == "POST":
            print(request.POST)
            newContact = Contact(user = user  ,  comment = request.POST["comment"] , requestType = request.POST["requestType"], evaluation = request.POST["evaluation"] )
            newContact.save()
            return redirect("main:homePage")

        return render(request, "main/contact.html" )
    except Exception as e:
        return render(request, "main/not_found.html")
    
def about(request : HttpRequest):

    return render(request ,"main/about.html")

def thank(request : HttpRequest):

    return render(request ,"main/thankPage.html")

def displayContact(request : HttpRequest):
    if not request.user.is_staff:
        return render(request, "main/not_authorized.html", status=401)
    
    contact = Contact.objects.all()

    return render(request ,"main/displayContact.html", {"contact" : contact})


