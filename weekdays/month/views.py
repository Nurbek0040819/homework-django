from django.shortcuts import render

# Create your views here.
month_list = ['January', 'february', 'march', 'april', 'may', 'june', 'august', 'september', 'october', 'november', 'december']

def month_view(request):
    return render(request, 'month/month.html', context={'oylar': month_list})
