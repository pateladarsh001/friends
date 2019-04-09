from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'friend'

urlpatterns = [
    path('', views.friend_view, name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
