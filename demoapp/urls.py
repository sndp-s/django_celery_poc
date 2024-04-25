from django.urls import path
from . import views

urlpatterns = [
    path('celery-async-task', views.demo_view),
]
