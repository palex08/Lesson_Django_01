from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
    path('about/', views.about_view, name='about'),
]
