from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users


def index(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('display')
    else:
        form = UsersForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def display(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'display.html', context)
