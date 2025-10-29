from django.shortcuts import render

# render home page
def home(request):
    return render(request, 'pages/home.html')
