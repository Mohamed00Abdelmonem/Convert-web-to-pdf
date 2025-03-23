from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display/', views.display_data, name='display_data'),
    path('download/', views.download_pdf, name='download_pdf'),
]