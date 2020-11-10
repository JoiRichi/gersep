from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import  Loginform, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .intern_details import intern_first_name, intern_candidate_code, intern_last_name
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

    print(name)
    context={'name': name.capitalize(),
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
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from accounts.utils import render_to_pdf #created in step 4

# Create your views here

class GeneratePDF(View):

    def get(self, request, *args, **kwargs):
        first_name = intern_first_name.get(str(request.user))
        last_name = intern_last_name.get(str(request.user))
        candidate_code = intern_candidate_code.get(str(request.user))
        template = get_template('index.html')
        context = {'firstname': first_name.capitalize(),
                   'lastname': last_name.capitalize(),
                   'code': candidate_code,
                   }
        html = template.render(context)
        pdf = render_to_pdf('index.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Gersep.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

def makePdf(email_list):
    for emails in email_list.keys():
        first_name = intern_first_name.get(emails)
        last_name = intern_last_name.get(emails)
        candidate_code = intern_candidate_code.get(emails)
        template = get_template('index.html')
        context = {'firstname': first_name.capitalize(),
                   'lastname': last_name.capitalize(),
                   'code': candidate_code,
                   }
        html = template.render(context)
        pdf = render_to_pdf('index.html', context)
        import email, smtplib, ssl

        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        subject = "An email with attachment from Python"
        body = "This is an email with attachment sent from Python"
        sender_email = "management.isscir@gmail.com"
        receiver_email = "lordrichado@gmail.com"
        password = input("jo1r1ch1")

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = "document.pdf"  # In same directory as script

        # Open PDF file in binary mode
        with open(pdf, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            print('sent')

email_list={
    'lordrichado@gmail.com': 'Richard Olumide Daodu'
}
def certPage(request):
    first_name = intern_first_name.get(str(request.user))
    last_name = intern_last_name.get(str(request.user))
    candidate_code = intern_candidate_code.get(str(request.user))
    template = get_template('index.html')
    context = {'firstname': first_name.capitalize(),
               'lastname': last_name.capitalize(),
               'code': candidate_code,
               }
    return render(request, 'index.html', context)