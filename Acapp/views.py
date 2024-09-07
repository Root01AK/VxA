# Crafted by Vcraftyu
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from operator import index
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Avinyacontact
from .models import Avinyacollab

# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def gallery(request):
    return render(request,'gallery.html')

def latestprojects(request):
    return render(request,'latestprojects.html')


def completedprojects(request):
    return render(request,'completedprojects.html')

def clothing(request):
    return render(request,'clothing.html')

def hilton(request):
    return render(request,'hilton.html')

def hyatt(request):
    return render(request,'hyatt.html')

def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('Name','')
        Number = request.POST.get('Number','')
        Email = request.POST.get('Email','')
        Message = request.POST.get('Message','')
        
        if Name and Number and Email and Message:
            
            Avinyacontact.objects.create(
                Name=Name,
                Number=Number,
                Email=Email,
                Message=Message
            )
            
            # Prepare the email content
            email_subject = 'Contact Form Submission - Clients or Visitors'
            html_message = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                <h2 style="color: #2C3E50;">New Contact Form Submission</h2>
                <p style="font-size: 16px; color: #34495E;"><strong>First Name:</strong> {Name}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Phone Number:</strong> {Number}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Email:</strong> {Email}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Message:</strong></p>
                <p style="padding: 10px; background-color: #F9F9F9; border: 1px solid #DDDDDD;">{Message}</p>
            </body>
            </html>
            """
            plain_message = strip_tags(html_message)
    # Strip HTML tags for plain text version
            email = EmailMultiAlternatives(
                subject=email_subject,
                body=plain_message,  # Plain text fallback
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL]
            )
            email.attach_alternative(html_message, "text/html")

# Send the email
            email.send(fail_silently=False)
            
            messages.success(request, 'Your message has been sent. We will get in touch soon.')

            return redirect('contact')
        
    return render(request,'contact.html')


def collaboration(request):
    if request.method == 'POST':
        Firstname = request.POST.get('Firstname','')
        Lastname = request.POST.get('Lastname','')
        Email = request.POST.get('Email','')
        Phone = request.POST.get('Phone','')
        CompanyName = request.POST.get('CompanyName','')
        Industry = request.POST.get('Industry','')
        Comments = request.POST.get('Comments','')
        email_opt_in = 'emailOptIn' in request.POST
        phone_opt_in = 'phoneOptIn' in request.POST
        
        if Firstname and Lastname and Email and Phone:
            
            Avinyacollab.objects.create(
                Firstname=Firstname,
                Lastname=Lastname,
                Email=Email,
                Phone=Phone,
                CompanyName=CompanyName,
                Industry=Industry,
                Comments=Comments 
            )
            # Prepare the email content
            email_subject = 'Request for Collaboration - Clients or Visitors'
            html_message = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                <h2 style="color: #2C3E50;">New Contact Form Submission</h2>
                <p style="font-size: 16px; color: #34495E;"><strong>First Name:</strong> {Firstname}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Last Name:</strong> {Lastname}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Email:</strong> {Email}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Phone:</strong> {Phone}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>CompanyName:</strong> {CompanyName}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Industry:</strong> {Industry}</p>
                <p style="font-size: 16px; color: #34495E;"><strong>Comments:</strong></p>
                <p style="padding: 10px; background-color: #F9F9F9; border: 1px solid #DDDDDD;">{Comments}</p>
            </body>
            </html>
            """

            # Strip HTML tags for plain text version
            plain_message = strip_tags(html_message)

            # Send an email to the email address specified in settings.EMAIL_HOST_USER
            email = EmailMultiAlternatives(
                subject=email_subject,
                body=plain_message,  # Plain text fallback
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL]
            )
            email.attach_alternative(html_message, "text/html")

# Send the email
            email.send(fail_silently=False)
            
            messages.success(request, 'Your message has been sent. We will get in touch soon.')
            return redirect('collaboration')
            
    return render(request,'collaboration.html')