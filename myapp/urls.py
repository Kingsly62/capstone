from myapp import views
from django.urls import path
from django.contrib.auth import views as auth
from myapp import views as user_view


urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name='index'),

    path('login/', user_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/', user_view.register, name='register'),
]
