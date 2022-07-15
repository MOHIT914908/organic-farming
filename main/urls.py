from django.urls import path
from main import views
urlpatterns = [
    path('', views.index, name='index'),
    path('achivement/', views.achivement, name='achivement'),
    path('fairs', views.fairs, name='fairs'),
    path("shops/",views.shops, name='shops'),
    path("contact/",views.contact, name='contact'),
    path("about",views.about,name='about'),
]