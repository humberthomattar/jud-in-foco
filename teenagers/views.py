
import logging
from .forms import TeenagerForm
from .models import Teenager
from django.shortcuts import render
from django.contrib import messages
# Create your views here.

logger = logging.getLogger('django')


def teenagers_list(request):
    teenagers = Teenager.objects.all()
    return render(request, 'teenagers/teenagers.html', {'teenagers': teenagers})

def teenager_new(request):
    if request.method == "POST":
        teenager = TeenagerForm(request.POST)
        if teenager.is_valid():
            teenager.save()
            messages.success(request, 'Adolescente cadastrado com sucesso.')
        else:
            messages.warning(request, 'Falha no cadastro')
    form = TeenagerForm()
    return render(request, 'teenagers/teenager_new.html', {'form': form})


def teenager_edit(request, pk):
    try:
        teenager = Teenager.objects.get(pk=pk)
        form = TeenagerForm(request.POST, instance=teenager) or None
        logger.info(str(request.POST))
        if request.method == 'POST':
            if form.is_valid():
                teenager = form.save()
                messages.success(request, 'Dados do(a) adolescente alterado`s com sucesso.')
            else:
                messages.warning(request, 'Falha na alteração. Formulário Inválido.')
    except Exception as e:
            messages.warning(request, 'Falha na alteração. Detalhe: +' + str(e))
    return render(request, 'teenagers/teenager_edit.html', {'form': form, 'teenager': teenager})
    

def teenager_change_status(request, pk):
    try:
        if request.method == "POST":
            teenager = Teenager.objects.get(pk=pk)
            if teenager.is_active:
                teenager.is_active = False
            else:
                teenager.is_active = True
            teenager.save()
            messages.success(request, 'Situação do(a) adolescente alterada com sucesso.')
    except Exception as e:
        messages.warning(request, 'Falha. Detalhe: +' + str(e))
    teenagers = Teenager.objects.all()
    return render(request, 'teenagers/teenagers.html', {'teenagers': teenagers})
    
