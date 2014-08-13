from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from main_app.models import *
from portfolio.models import Project
from main_app.forms import ContactForm
from django.contrib.auth.models import User, BaseUserManager
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
import os
from postmark import PMMail
from diana_website import settings
from django.contrib import messages
def home(request):   
    category = get_object_or_404(Category, position=1)
    content = category.content_set.first()
    
    
    return render(request, 'base.html', {'item' : content})



def index(request, catSlug):
    
    c = get_object_or_404(Category, position__gt=1, slug=catSlug, type="")
    
    
    return render(request, 'index.html', locals())

@csrf_protect
def contact(request):
    if request.method == "POST":
        # send the data to the form 
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            senderName = contact_form.cleaned_data['senderName']
            cc_myself = contact_form.cleaned_data['cc_myself']
            senderEmail = contact_form.cleaned_data['senderEmail']
            
            #===================================================================
            # #if the contact does not exist, we create it
            # try:
            #     contact = Contact.objects.get(pk=senderEmail)
            # except Contact.DoesNotExist:
            #     contact = Contact(email = senderEmail,name = senderName )
            #     contact.save()
            #===================================================================
                
            dest = User.objects.get_by_natural_key("matthieu")
            print dest.email
            recipients = [dest.email]
            cc = ""
            if cc_myself:
                cc = senderEmail
                recipients.append(senderEmail)
            #send_mail(subject, message, senderEmail, recipients)
            #===================================================================
            # message = PMMail(api_key = settings.API_POSTMARK,
            #      subject = subject,
            #      sender = senderEmail,
            #      to = dest.email,
            #      text_body = message,
            #      Cc = cc,
            #      )
            # message.send()
            #===================================================================
            
            messages.success(request, '<div class="success">Your email has been sent!!</div>')
    else:    
        # send a empty form
        contact_form = ContactForm()
        
    return render(request, 'contact.html', {'form': contact_form})
