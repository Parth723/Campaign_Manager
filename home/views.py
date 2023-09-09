from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Subscriber
from django.contrib import messages

from django.core import mail
from django.template.loader import render_to_string
from home.models import Campaign
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def subscribe(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        is_active = request.POST.get('is_active')== 'true'
        subs = Subscriber(name=name, email=email, is_active=is_active)
        subs.save()
        messages.success(request, "Subscription successful.")
        return redirect('confirmation')

    return render(request, "subscribe.html")

def send_campaign_email(request):
    
    active_subscribers = Subscriber.objects.filter(is_active=True)

    campaign_subject = 'Save the Soil'

    campaign = Campaign.objects.get(subject=campaign_subject)

    for subscriber in active_subscribers:
            subject = campaign.subject
            from_email = "jarvis7723@gmail.com" 
            to_email = subscriber.email

            email_content = render_to_string('email_base.html', {'campaign': campaign})

            email_message = mail.EmailMessage(
                subject, email_content, from_email, [to_email])

            email_message.content_subtype = "html"
            email_message.send()

    return render(request, 'email_sent.html')


def confirmation(request):
     return render(request, 'confirmation.html')
