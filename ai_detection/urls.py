from django.urls import path

from .views import detect_defects


urlpatterns = [

    path(
        'detect/',
        detect_defects,
        name='detect_defects'
    ),

]