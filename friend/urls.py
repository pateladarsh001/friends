from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'friend'

urlpatterns = [
    path('', views.friend_view, name='index'),
    path('create-friend', views.FriendCreateView.as_view(), name='create-friend'),
    path('<int:pk>/update-friend', views.FriendUpdateView.as_view(), name='update-friend'),
    path('<int:pk>/delete-friend', views.FriendDeleteView.as_view(), name='delete-friend'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
