from django.urls import path

from bewell.views import home,survey

app_name = "bewell"
urlpatterns = [
    path('',home,name='home'),
    path('survey/',survey,name='survey'),
]
