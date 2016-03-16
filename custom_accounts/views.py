from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegistrationForm
from .forms import contact_us_form
from .models import User


def RegistrationView(request):
    contact_form = contact_us_form()
    form = RegistrationForm()

    context = {"title" : "Subscribe for our newsletter and initial offers",
               "form":form,
               "contact_form" : contact_form,
               "contact_title" : "Let us know what you think to create a better service",
               }

    if 'Registration' in request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():

            obj = form.save(commit=False)
            obj.set_password(User.objects.make_random_password())
            obj.save()

            ##sending mail to the registered users

            subject = 'Mr buch Newsletter'
            from_mail = settings.EMAIL_HOST_USER
            to_email = str(obj)
            # print to_email
            email_message = "Thanks for subscribing with Mr Buch. Our site will be functonal very soon. Till then call us to rent books on 7768982321 and enjoy our initial offers."
            send_mail(subject,
                      email_message,
                      from_mail,[to_email],
                      fail_silently=True)
            context = {
                "title":'Thank you, You have been Subscribed',
                "contact_form" : contact_form,
                "contact_title" : "jgjgwfwhj",

            }
    elif 'Contact' in request.POST:
        contact_form = contact_us_form(request.POST)

        if contact_form.is_valid():
            email = contact_form.cleaned_data.get('email')
            subject = 'Meesage from Contact Us from %s' %(email)
            message = contact_form.cleaned_data.get('message')
            to_email = settings.EMAIL_HOST_USER
            from_mail = settings.EMAIL_HOST_USER
            print email
            send_mail(subject,
                      message,
                      from_mail,[to_email],
                      fail_silently=True)

            context = {"title" : "Subscribe for our newsletter and initial offers",
                       "form":form,
                    #    "contact_form" : contact_form,
                       "contact_title" : "We are happy to listen your request.",
                       }

    return render(request,'custom_layout.html',context)
