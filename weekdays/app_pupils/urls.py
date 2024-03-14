from django.urls import path

from .views import pupils_view, pupil_view

urlpatterns = [
        path('pupils/', pupils_view, name='pupils'),
        path('pupils/i', pupil_view, name='pupil'),
]