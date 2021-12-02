from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html", context={})

def contact(request):
    return render(request, "contact.html", context={})

def about(request):
    return render(request, "about.html", context={})
