from django.shortcuts import render,HttpResponse

# Create your views here.
def example(request):
    return render(request, 'index.html')
    # return HttpResponse("this is sample page")

def about(request):
    return HttpResponse("this is about page")

def service(request):
    return HttpResponse("this is sample page")

def contact(request):
    return HttpResponse("this is sample page")