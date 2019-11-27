from .forms import UserForm
import logging
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

logger = logging.getLogger('django')


def users_list(request):
    users = User.objects.all()
    return render(request, 'accounts/users.html', {'users': users})

def user_new(request):
    try:
        if request.method == "POST":
            user = UserForm(request.POST)
            if user.is_valid():
                user = user.save(commit=False)
                user.password = make_password(user.password)
                user.save()
                messages.success(request, 'Usuário cadastrado com sucesso.')
            else:
                messages.warning(request, 'Falha no cadastro')        
    except Exception as e:
        messages.warning(request, 'Falha no cadastro. Detalhe: +' + str(e))
    form = UserForm()
    return render(request, 'accounts/user_new.html', {'form': form})



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha alterada com sucesso')
        else:
            messages.warning(request, 'Falha na alteração da senha. Por favor, observe as orientações acima.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


def user_change_is_active(request, pk):
    try:
        if request.method == "POST":
            user = User.objects.get(pk=pk)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
            messages.success(request, 'Situação da conta alterada com sucesso.')
        else:
            messages.warning(request, 'Falha. Detalhe: +' + str(e))    
    except Exception as e:
        messages.warning(request, 'Falha. Detalhe: +' + str(e))
    users = User.objects.all()
    return render(request, 'accounts/users.html', {'users': users})

