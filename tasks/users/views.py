from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.views import View
from django.urls import reverse
from django.contrib import messages

class SignupView(View):
    form_class=UserRegistrationForm
    template_name='signup.html'
    def get(self,request):
        form=self.form_class()
        context={'form':form}

        return render(request,self.template_name,context)

    def post(self,request):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,message='User Created Successfully')
            return redirect(reverse('login'))
        
        context={'form':form}

        return render(request,self.template_name,context)
 
   #         <a href="{% url 'logout' %}">Log Out</a>