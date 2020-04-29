from django.urls import path

from bear import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('student/', views.student, name='student'),
    path('logout/', views.logout, name='logout'),
    path('reset/', views.reset, name='reset'),
    path('reset_pwd/', views.reset_pwd, name='reset_pwd')
]
