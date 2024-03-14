from django.urls import path

from .views import month_view
urlpatterns = [
        path('', month_view, name='month_list')
]