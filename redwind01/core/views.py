from django.shortcuts import render
# Create your views here.
# need to add to core.views and redwind01.urls


def frontpage(request):
    return render(request, 'core/frontpage.html')

def about(request):
    return render(request, 'core/about.html')

def about(request):
    return render(request, 'core/test.html')

