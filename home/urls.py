from django.urls import path
from .views import (home,create,read,update,delete,)
urlpatterns = [
    path('', home , name= 'home'),
    path('create/', create , name= 'create'),
    path('read/<id>', read , name= 'read'),
    path('update/<id>', update , name= 'update'),
    path('delete/<id>',delete,name='delete')

]
