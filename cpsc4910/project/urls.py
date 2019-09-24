from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('reset/', views.ResetView.as_view(), name='reset'),
]