from django.urls import path
from . import views


urlpatterns = [
    
    path('home',views.HomeView.as_view()),#changed according to class view
    path('authorize',views.AuthorizedView.as_view()),
]