from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('new_page',views.new_page,name='new_page'),
    path('new_form',views.new_form,name='new_form'),
    path('logout',views.logout,name='logout')

]