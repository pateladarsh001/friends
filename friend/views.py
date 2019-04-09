from django.shortcuts import render
from .models import Friend
# Create your views here.


def friend_view(request):
    friends = Friend.objects.all()
    return render(request, 'friend/index.html', {'friends': friends})
