from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# you can delete these later
# from django.contrib.auth.models import User

# to show messages, we need to import the messages
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    '''
    So what's happening here is that these 2 lines:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})
    make the form and show it on screen, and when the user clicks on that little 
    register button, it comes in this function againa and runs those 2 lines again.
    We don't want that, when the user clicks "register" (or POSTS the information) we
    want to take that information, save it and then show another page.
    '''
    if request.method == 'POST':
        # here i think we take in the data sumbitted from the post method
        form = RegisterForm(request.POST)

        # check form validity, it also checks for unique usernames
        if form.is_valid():
            # let's save the user also
            form.save()

            # now we want to show a message with the username, so we get the username
            username = form.cleaned_data.get('username')

            # to display a success message
            # ok so you have to include this message in a webpage, otherwise it won't show
            # so we include the message thing in the base.html file
            messages.success(request, f"Welcome {username}, your account is created!")
            # return redirect('login')
            return render(request, 'registration/login.html')

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form':form})



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'