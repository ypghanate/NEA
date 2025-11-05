from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_view, name='upload'),
    path('result/<int:pk>/', views.result_view, name='result'),
    path('upload/', views.upload_view, name='upload_audio'),
]
