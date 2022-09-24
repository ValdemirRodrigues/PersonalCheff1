from django.shortcuts import render

def index(request):
    receitas={
        1:'Suco de Melão',
        2:'Pizza',
        3:'Suco de Caju'
    }
    dados ={
        'lista_receitas': receitas
    }
    return render(request,'index.html',dados)

def sucodelaranja(request):
    return render(request, 'sucodelaranja.html')
def sucodelimao(request):
    return render(request, 'sucodelimao.html')
def sucodemorango(request):
    return render(request, 'sucodemorango.html')
def contato(request):
    return render(request, 'contato.html')