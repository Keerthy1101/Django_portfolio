from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('project/<str:project_id>/', views.project_detail, name='project_detail'),

]
