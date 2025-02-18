from . import views
from django.urls import path

app_name='test_app'

urlpatterns = [
    path('',views.home,name='main')
]
