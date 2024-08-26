from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_view),
    path('test', views.test_view),
]
