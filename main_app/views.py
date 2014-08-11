from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from main_app.models import *
from portfolio.models import Project
from main_app.forms import ContactForm
from django.contrib.auth.models import User, BaseUserManager
from django.views.decorators.csrf import csrf_protect

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
            recipients.append(dest.email);
            if cc_myself:
                recipients.append(senderEmail)
            send_mail(subject, message, senderEmail, recipients)

    else:    
        # send a empty form
        contact_form = ContactForm()
        
    return render(request, 'contact.html', {'form': contact_form})
