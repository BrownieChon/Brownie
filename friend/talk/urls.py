from django.urls import path
from . import views

urlpatterns = [
    path('', views.talk, name='index'),
    path('register/', views.member, name='index'),
    path('register/regist/', views.regist,),
    path('login/', views.login,),
    path('login/log/', views.log,),
    path('login/log/comment/', views.add, name='add'),

]