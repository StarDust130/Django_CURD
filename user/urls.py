
from django.urls import path
from .views import login , create_user 

urlpatterns = [
    path('', create_user.as_view(), name='create_user'),
    path('login/', login.as_view(), name='login'),

]
