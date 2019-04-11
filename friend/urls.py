from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name = 'friend'

urlpatterns = [
    path('', views.FriendView.as_view(), name='index'),
    path('create-friend', views.FriendCreateView.as_view(), name='create-friend'),
    path('<int:pk>/update-friend', views.FriendUpdateView.as_view(), name='update-friend'),
    path('<int:pk>/delete-friend', views.FriendDeleteView.as_view(), name='delete-friend'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

]

