from django.shortcuts import render

# Create your views here.
themes = ['', 'Online store bot', 'HTML va CSS', 'Bootstrap', 'Javascript', 'Introduction to Django', 'Django views and urls', 'Temlates and Static files', 'Imtihon']

def themes_view(request):
    return render(request, 'themes/themes.html', context={'mavzular': themes})
