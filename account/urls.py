from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.RegisterUser.as_view(),name='register'),
    path('login/',views.LoginUser.as_view(),name='login'),
    path('preference/',views.Prefrence.as_view(),name='prefrence'),

]