from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm
import datetime

# Create your views here.

def home(request):
    data = {} #dicionario
    data['transacoes'] = ['Dantas', 'Dudu(gay)', 'Dudu(torto,golandense)']
    data['now'] = datetime.datetime.now() # adicionei um valor a variavel e passar ela como argumento para a view

    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

    return render(request, 'contas/home.html', data) # passando a variavel como argumento para a view
    #proximo passo é usar ela no template relacionado a view, que no caso é contas\home


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all() # ao implementar um model(transacao) o django ja cria um manager para ele
    # oque seria um manager ? é basicamente um entity.manager do jpa, que tem funções de banco de dados, como o all acima, que tras todos
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form

    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete() 
    return redirect('url_listagem')