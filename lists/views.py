from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def homepage(request):
    #html = "<html><title>To-Do lists</title></html>"
    return render(request, 'home.html')
