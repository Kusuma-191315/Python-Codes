from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name = 'hello'),
    path('open_signup', views.open_signup,  name = 'open_signup'),
    path('open_signin', views.open_signin,  name = 'open_signin'),
    path('signup', views.signup,  name = 'signup'),
]