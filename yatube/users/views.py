from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm, ProfileForm, UserForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


@login_required
@transaction.atomic
def update_profile(request):
    user_form = UserForm(
        request.POST or None,
        instance=request.user)
    profile_form = ProfileForm(
        request.POST or None,
        files=request.FILES or None,
        instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        print('Ваш профиль был успешно обновлен!')
        return redirect('posts:user_profile', request.user)
    else:
        print('Пожалуйста, исправьте ошибки.')

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
