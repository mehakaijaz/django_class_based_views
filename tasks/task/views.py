from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.
""" function based views
def home(request):
    tasks=Task.objects.all()
    context={
        'tasks':tasks
    }
    return render(request,'index.html',context)

def add_task(request):
    form=TaskCreateForm()

    if request.method=='POST':
       form=TaskCreateForm(data=request.POST)

       if form.is_valid():
           form.save()
           return redirect(reverse('homepage')) 
    return render(request,'add.html',{'form':form})
def view_task(request,task_id):
    task=Task.objects.get(id=task_id)
    context={
        'task':task
    }
    return render(request,'detail.html',context)

def update_task(request,task_id):
    task=Task.objects.get(id=task_id)
    form=TaskCreateForm(instance=task)
    if request.method=='POST':
        form=TaskCreateForm(instance=task,data=request.POST)
        if form.is_valid():
           form.save()
        return redirect(reverse('homepage')) 
    context={
        'form':form
    }
    
    return render(request,'update.html',context)

def delete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect(reverse('homepage')) """

from django.views import View

'''CLASS BASED VIEWS WITH FUNCTIONS:
class HomePageView(View):#basic class based view with function(get,post) in it
    template_name='index.html'
    
    def get(self,request):
        tasks=Task.objects.all()
        context={
            'tasks':tasks
        }
        return render(request,'index.html',context)
    
class TaskCreateView(View):
    template_name='add.html'
    form_class=TaskCreateForm
    initial={'key':'value'}

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class(initial=self.initial)})

    def post(self,request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('homepage'))
        return render(request,self.template_name,{'form':self.form_class(initial=self.initial)})
    
class TaskDetailView(View):
    template_name='detail.html'

    def get(self,request,task_id):
       task=Task.objects.get(id=task_id)
       return render(request,self.template_name,{'task':task})
class TaskUpdateView(View):
    template_name='update.html'
    form_class=TaskCreateForm

    def get(self,request,task_id):
        task=Task.objects.get(id=task_id)
        form=self.form_class(instance=task)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,task_id):
        task=Task.objects.get(id=task_id)   
        form=self.form_class(instance=task,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('homepage'))
        return render(request,self.template_name,{'form':form})
    
class TaskDeleteView(View):
    def get(self,request,task_id):
        task=Task.objects.get(id=task_id)
        task.delete()
        return redirect(reverse('homepage'))  
    
class SettingsView(View):
    template_name='settings.html'
    def get(self,request):
        return render(request,self.template_name)'''

#generic based views :
from django.views.generic import (
    #displayviews
    TemplateView,
    ListView,
    DetailView,

    #editviews
    FormView,UpdateView,
    CreateView,
    DeleteView
)
#ye template view h isme ese code hota h
'''class HomePageView(TemplateView):
    template_name='index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=Task.objects.all()
        return context'''

class HomePageView(ListView):
    template_name='index.html' 
    model=Task 
    context_object_name='tasks'

#ye form view h isme ese code hota h
'''class TaskCreateView(FormView):
    template_name='add.html'
    form_class=TaskCreateForm
    success_url='/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)'''

class TaskCreateView(CreateView):
    template_name='add.html'
    model=Task 
    success_url='/'
    fields=['name','description']

class TaskDetailView(DetailView):
    template_name='detail.html'
    model=Task
    context_object_name='task'

class TaskUpdateView(UpdateView):
    template_name='update.html'
    model=Task
    fields=['name','description']
    success_url='/'

class TaskDeleteView(DeleteView):
    template_name='delete.html'
    model=Task
    success_url='/'
class SettingsView(View):
    template_name='settings.html'
    def get(self,request):
        return render(request,self.template_name)