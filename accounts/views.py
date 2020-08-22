from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import  Loginform, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .intern_details import intern_first_name, intern_candidate_code
from django.contrib.auth.decorators import login_required



def pagelogin(request):
   # uservalue = ''
   # passwordvalue = ''

    form = Loginform(request.POST or None)
    if form.is_valid():

        uservalue = form.cleaned_data.get("email")

        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)


            context = {'user': uservalue,
                       'error': 'The login has been successful',

                       }

            return redirect('/logged_in', context)
        else:
            context = {'form': form,
                       'error': 'The username and password combination is incorrect'}

            return render(request, 'login.html', context)

    else:
        context = {'form': form}
        return render(request, 'login.html', context)

@login_required(login_url='/login') #redirect when user is not logged in
def student_page(request):

    name = intern_first_name.get(str(request.user))
    candidate_code = intern_candidate_code.get(str(request.user))
    name1= name.capitalize()
    print(name)
    context={'name': name1,
             'code': candidate_code,
              }
    return render(request, 'welcome.html', context)

def student_sign_up(request):

    form = CustomUserCreationForm(request.POST or None)
    print(form)
    if form.is_valid(): #and form.username in users_info.keys():
        username = form.cleaned_data['email']
        if username in intern_candidate_code.keys():
            form.save()
            return redirect('/login')
        else:
            context = {
                'form': form, 'error': 'You are not a prospective candidate!!'
            }
            return render(request, 'signup.html', context)

    else:
        context = {
            'form': form
        }
        return render(request, 'signup.html', context)

def get_name(user):
    user_name= intern_first_name.get(user)
    return user_name
def get_code(user):
    user_code = intern_candidate_code(user)
    return user_code