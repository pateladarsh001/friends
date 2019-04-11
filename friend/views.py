from django.shortcuts import render, redirect
from .models import Friend
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class FriendView(LoginRequiredMixin, ListView):
    model = Friend
    context_object_name = 'friends'
    template_name = 'friend/index.html'

    def get_queryset(self):
        return Friend.objects.filter(user=self.request.user)


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


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('friend:index')
    return render(request, 'friend/signup.html', {'form': form})


