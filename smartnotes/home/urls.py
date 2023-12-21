from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.HomeView.as_view(), name='home'),#changed according to class view
    #path('authorize',views.AuthorizedView.as_view(), name=''),
    path('login',views.LoginInterfaceView.as_view(), name='login'),
    path('logout',views.LogoutInterfaceView.as_view(), name='logout'),

]