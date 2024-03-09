from django.urls import path
from .views import index, about, nurbek1,nurbek2
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('nurbek1/', nurbek1, name='nurbek'),
    path('nurbek2/', nurbek2, name='nurbekjan'),
]