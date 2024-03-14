from django.urls import path

from .views import themes_view
urlpatterns = [
        path('themes/', themes_view, name='themes')
]