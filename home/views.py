from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import (CRUD,)
from .forms import (CrudForm,)
# Create your views here.
def home(request):
    crud = CRUD.objects.all()
    return render(request, 'index.html', {'cruds':crud})

def create(request):
    if request.method == 'POST':
        forms = CrudForm(request.POST) # creates form instance via POST method 
        if forms.is_valid():    # checks if the form is valid or not
            forms.save()        #save data in database
            return redirect('home')
        else:
            return HttpResponse("form isn't valid.")
    
    form = CrudForm() # creates form instance to load form via get method

    return render(request, 'create.html', {'forms':form})

def read(request,id):
    crud = CRUD.objects.get(id=id)

    return render(request, 'read.html',{'crud': crud})

def update(request,id):
    crud = CRUD.objects.get(id=id)
    forms = CrudForm(instance=crud)
    if request.method == 'POST':
        forms = CrudForm(request.POST, instance= crud) # creates form instance via POST method 
        if forms.is_valid():    # checks if the form is valid or not
            forms.save()        #save data in database
            return redirect('home')
        else:
            return HttpResponse("form isn't valid.")
        
    
    return render(request, 'update.html',{'forms':forms})


def delete(request,id):
    crud = CRUD.objects.get(id=id)
    crud.delete()
    return redirect('home')
    