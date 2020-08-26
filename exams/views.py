from django.shortcuts import render, redirect
from .forms import ExamForm, GetUsers
from django.utils import timezone
from .models import Submission
from accounts.intern_details import intern_candidate_code, intern_first_name
# Create your views here.
from django.contrib.auth.decorators import login_required

submitted_list= []

@login_required
def assignment_page(request):
    form = ExamForm(request.POST or None)


    if form.is_valid():
        question = form.cleaned_data['question']
        email = form.cleaned_data['email']
        if question.deadline > timezone.now():
            if email == request.user:
                if str(email) not in submitted_list:
                    submitted_list.append(str(email))
                    form.save()
                    return redirect('/success', {})
                else:
                    context = {
                        'form': form, 'error': 'You have already submitted, please wait for further instructions from the Director. Best of Luck.'
                    }
                    return render(request, 'exam_page.html', context)
            else:
                context = {
                    'form': form, 'error': 'You cannot do this exam for another person! Please select your email.'
                }
                return render(request, 'exam_page.html', context)
        else:
            context = {
                'form': form, 'error': 'The deadline has Exceeded!, please feel free to re-apply next time.'
            }
            return render(request, 'exam_page.html', context)


    else:
        context = {
                'form': form
            }
        return render(request, 'exam_page.html', context)


def success_page(request):
    context ={}
    if request.user in submitted_list:
        context ={
            'name': intern_first_name.get(str(request.user)),
            'code': intern_candidate_code.get(str(request.user))
            }
    return render(request, 'success.html', context)


def get_candidate_code():
    candidate_codes=[]
    for people in submitted_list:
        candidate_codes.append(intern_candidate_code.get(people))
    return candidate_codes



def get_list_of_submission(request):

    form= GetUsers(request.POST or None)
    if form.is_valid():
        email= form.cleaned_data['email']
        email_a=email.lower()
        submitted_list.remove(str(email_a))
        context= {'list': submitted_list, 'form': form, 'code': get_candidate_code()}
        return render(request, 'submission_list.html', context)
    else:
        context = {'list': submitted_list, 'form': form, 'code': get_candidate_code()}
        return render(request, 'submission_list.html', context)


def get_scores(request):
    submissions = Submission.objects.all()
    return render(request, 'scores.html', {'submissions': submissions} )