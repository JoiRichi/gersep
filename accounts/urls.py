from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index_page, name='index_page'),
    path('login', views.pagelogin, name='login_up'),
    path('logged_in', views.student_page, name='account'),
    path('signup', views.student_sign_up, name='signup'),
]