from django.shortcuts import render, redirect
# from django.contrib.auth.forms import CreateUserForm
from .forms import CreateUserForm
# Create your views here.
from django.contrib import messages

def user_registration(request):
    form = CreateUserForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'User with username '+str(instance.username)+' created successfully!!')
            return redirect('home')
    context = {'form':form}
    return render(request, 'register.html', context)
