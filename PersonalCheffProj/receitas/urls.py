from django.urls import path
from . import views
urlpatterns = [
     path('', views.index, name='index'),
     path('sucodelaranja', views.sucodelaranja, name='sucodelaranja'),
     path('contato', views.contato, name='contato'),
     
     path('sucodelimao', views.sucodelimao, name='sucodelimao'),
     path('sucodemorango', views.sucodemorango, name='sucodemorango')
     
    ]