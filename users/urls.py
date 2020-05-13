from . import views
from django.views.generic import ListView


from django.urls import path

urlpatterns = [
    path('register/',views.register),
    path('login/',views.logins),
    path('logout/',views.LogoutFormView.as_view()),
]
