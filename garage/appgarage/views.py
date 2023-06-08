from django.shortcuts import render, HttpResponseRedirect
from . import forms
from . import models


# Create your views here.
def add_Auto(request):
    form = forms.Auto_Form
    return render(request, 'appgarage/add_auto.html', {"form" : form})

def update_Auto(request,id):
    auto = models.auto.objects.get(pk=id)
    form = forms.Auto_Form(auto.__dict__)
    return render(request, 'appgarage/update_auto.html',{"form":form, "auto": auto})

def delete_Auto(request,id):
    categorie = models.auto.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/appgarage/")

def view_Auto(request, id):
    auto = models.auto.objects.get(pk=id)
    return render(request, 'appgarage/view_auto.html', {'auto': auto})

def view_all_Auto(request):
    liste = list(models.auto.objects.all())
    return render(request, 'appgarage/index.html',{'liste':liste})

def traitement(request):
    form = forms.Auto_Form(request.POST)
    if form.is_valid():
        auto = form.save()
        return render(request,"appgarage/view_auto.html",{"auto" : auto})
    else:
        return render(request,"appgarage/add_auto.html",{"form": form})
    
def traitement_update(request, id):
    auto1 = models.auto.objects.get(pk=id)
    form = forms.Auto_Form(request.POST)
    if form.is_valid():
        auto = form.save(commit=False) 
        auto.id = id; 
        auto.save() 
        return HttpResponseRedirect("/appgarage/") 
    else:
        return render(request, "appgarage/update_auto.html", {"form": form, "auto": auto1})
