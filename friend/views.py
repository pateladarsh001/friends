from django.shortcuts import render
from .models import Friend
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.


def friend_view(request):
    friends = Friend.objects.all()
    return render(request, 'friend/index.html', {'friends': friends})


class FriendCreateView(CreateView):
    model = Friend
    fields = ['name', 'age', 'residence', 'primary_school', 'high_school',
              'university', 'course', 'profession', 'hobbies', 'is_male', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FriendUpdateView(UpdateView):
    model = Friend
    fields = ['name', 'age', 'residence', 'primary_school', 'high_school',
              'university', 'course', 'profession', 'hobbies', 'is_male', 'image']


class FriendDeleteView(DeleteView):
    model = Friend
    success_url = '/'