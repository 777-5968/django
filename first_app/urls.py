from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('safari/',views.safari,name='safari'),
    path('home/',views.home,name='home')
]