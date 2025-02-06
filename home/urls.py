from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('main/', views.main_page, name='main_page'),
    path('upload_report/', views.upload_report, name='upload_report'),
    path('analysis/', views.analysis, name='analysis'),
    path('aboutus/',views.aboutUs, name='aboutUs'),
    path('contact/',views.contact, name='contact'),
]
