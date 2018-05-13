from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'myApp/index.html', context_dict)

def other(request):
    return render(request, 'myApp/other.html')


def relative(request):
    return render(request, 'myApp/relative_url.html')
