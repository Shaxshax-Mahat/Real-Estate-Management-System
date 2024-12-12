import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from requests.auth import HTTPBasicAuth
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from homeapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from homeapp.forms import ContactForm, ImageUploadForm
from homeapp.models import Contact, User, ImageModel
from django.contrib.auth import authenticate, login, logout

# @login_required
# def logout(request):
#     logout(request)
#     return redirect('login')


# def signin(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
#
#         user = authenticate(username=username, password=pass1)
#
#         if user is not None:
#             login(request, user)
#
#             if user.is_staff:
#                 messages.success(request, f"{username} - Logged In Successfully!!")
#                 return redirect('staff_dashboard')
#
#             messages.success(request, f"{username} - Logged In Successfully!!")
#             return redirect('students_dashboard')
#         else:
#
#             if User.objects.filter(username=username, is_active=False):
#                 messages.error(request, "Please Activate your account first.")
#                 return redirect('signin')
#
#             else:
#                 messages.error(request, "Invalid username or password.")
#                 return redirect('signin')
#     else:
#
#             return render(request, "login.html")


# Create your views here.
def index(request):
    if request.method == 'POST':
        user = User.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        ).exists()
        if user:

            return render(request, 'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def agents(request):
    return render(request,'agents.html')

def contact(request):
    if request.method == 'POST':
        mycontacts = Contact(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        mycontacts.save()
        return redirect('/show_contact')
    else:
        return render(request, 'contact.html')


def properties(request):
    return render(request,'properties.html')

def property_single(request):
    return render(request,'property-single.html')

def service_details(request):
    return render(request,'service-details.html')

def services(request):
    return render(request,'services.html')

def starter_page(request):
    return render(request,'starter-page.html')

def show_contact(request):
    allcontacts = Contact.objects.all()
    return render(request,'show-contact.html',{'contact':allcontacts})

def delete(request,id):
    deletecontact = Contact.objects.get(id=id)
    deletecontact.delete()
    return redirect('/show_contact')

def edit(request,id):
    editcontact = Contact.objects.get(id=id)
    return render(request,'edit.html',{'contact':editcontact})

def update(request,id):
    updateinfo = Contact.objects.get(id=id)
    form = ContactForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show_contact')
    else:
        return render(request,'edit.html')

def register(request):
    if request.method == 'POST':
        members = User(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'login.html')

@staff_member_required()
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
        return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


#Mpesa API views
def token(request):
    consumer_key = 'GVsxXZNDEYuHAKYGodv12CuBNUmvTDNcYArwQP7R6uPHcALB'
    consumer_secret = 'gxrX8EuH8daq0pPAsUfTA3GZFokZWpfKfNBXAvD3khUUwJ1vXYVBYeJ3OmZt5wtE'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request,):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Shaxshax",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment made successfully!")





