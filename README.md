# <nome_do_projeto>
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<img src="exemplo.jfif" alt="exemplo imagem">
> <Descrição do projeto>
Uma aplicação web de receitas chamada PersonalCheff1 desenvolvida durante o curso de Python no Senac Americana. A aplicação listará receitas e clicando em cada nome de receita você pode ver a receita completa.

### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
- [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code
- [X] Criar e ativar o ambiente virtual
```
criação e ativação
python -m venv .\venv\
Scripts\activate
```

- [X] Instalar de Django
```
python -m pip install django==3.2
```
- [X] Criar o projeto PersonalCheff1
```
Busca por comandos
django-admin help
django-admin.py help
django-admin.py startproject PersonalCheffProj
```
- [X] Subir o servidor e testar o projeto
```
entrar na pasta do projeto
cd PersonalCheffProj

executar o projeto no servidor 
python manage.py runserver
```
- [X] Criar e ativar o ambiente virtual 
- [X] Subir o servidor e testa o projeto 
- [X] Alterar o idioma do projeto para `pt-br` 

Abrir o arquivo `settings.py` e na linha 106 trocar `en-us` para `pt-br` 

- [X] Alterar o timezone do prpjeto para `America/Sao_Paulo`
Abrir o arquivo `settings.py` e na linha 108 trocar `UTC` para `America/Sao_Paulo`
- [X] Criar o app receitas
```
python manage.py startapp receitas  
```
- [X] Registrar  o app receitas
```
    no arquivo settings.py adicionar o app receitas na lista de apps 
INSTALLED_APPS[
    ...
    'receitas',
]
- [X] Configurar a rota inicial (index)
```
Dentro da pasta receita(app) criar o arquivo urls.py
no arquivo urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index')
    ]
```
- [X] Criar a view  para a rota inicial
```
Dentro da pasta receitas(app) abrir o arquivo views.py
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("<h1>Seja bem vindo</h1>")
```
- [] Registrar a rota inicial
- [] Criar arquivo index
-Dentro da pasta receitas(app), criar a pasta 'templetes'
- Dentro da pasta Templetes criar index.html
- No arquivo viwes.py que esta dentro da pasta do app faça a seguinte alteração de codigo:
```
    python
    

```


    

## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>