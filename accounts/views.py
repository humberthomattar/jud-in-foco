from .forms import UserForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

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
