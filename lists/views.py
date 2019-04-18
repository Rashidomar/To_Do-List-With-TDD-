from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    if request.method == 'post':
        return HttpResponse(request.POST['item'])
    #html = "<html><title>To-Do lists</title></html>"
    return render(request, 'home.html')
