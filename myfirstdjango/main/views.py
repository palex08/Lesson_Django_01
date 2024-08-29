from django.shortcuts import render

def home_view(request):
    return render(request, 'main/home.html')

def data_view(request):
    return render(request, 'main/data.html')

def test_view(request):
    return render(request, 'main/test.html')

def about_view(request):
    return render(request, 'main/about.html')
