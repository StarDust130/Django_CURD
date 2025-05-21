
from django.urls import path
from .views import LoginView , UserCreateView 

urlpatterns = [
    path('', UserCreateView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),

]
