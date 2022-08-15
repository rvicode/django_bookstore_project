from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('singe_up/', views.SingUpView.as_view(), name='singup'),
]