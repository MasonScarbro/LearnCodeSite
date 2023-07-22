from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from Main import views


urlpatterns = [
    path("", views.index, name='index')

]