from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from Main import views
from django.urls import path, include 


urlpatterns = [
    path("", views.index, name='index'),
    path("chatbot/", views.chatbot, name='chatbot'),
    path("chatTest/", views.chatTest, name='chatTest')

]