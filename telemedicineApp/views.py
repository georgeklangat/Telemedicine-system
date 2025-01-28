import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from telemedicineApp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from telemedicineApp.forms import AppointmentForm, ProductForm, ContactForm, ImagemodelForm
from telemedicineApp.models import Appointment, Product, Contact, User, ImageModel


def index(request):
    if request.method == "POST":
        if User.objects.filter(
                username=request.POST["username"],
                password=request.POST["password"]
        ).exists():
            return render(request, "index.html")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def service(request):
    return render(request, 'service-details.html')


def starter(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def myservice(request):
    return render(request, 'services.html')


# Create your views here.

def appointment(request):
    if request.method == "POST":
        myappointments = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        myappointments.save()
        return redirect('/appointment')
    else:
        return render(request, 'appointment.html')



def show(request):
    allapointments = Appointment.objects.all()
    products = Product.objects.all()
    allcontact = Contact.objects.all()
    return render(request, 'show.html', {
        'appointment': allapointments,
        'products': products,
        'contacts': allcontact
    })


def deleteappointment(request, id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')


def deleteproduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/show')


def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],

        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/show')


def editappointment(request, id):
    editappointment = Appointment.objects.get(id=id)
    return render(request, 'editappointment.html', {
        'appointment': editappointment
    })


def editproduct(request, id):
    editproduct = Product.objects.get(id=id)
    return render(request, 'editproduct.html', {
        'product': editproduct
    })


def editcontact(request, id):
    editcontact = Contact.objects.get(id=id)
    return render(request, 'editcontacts.html',
                  {'contact': editcontact
                   })


def updateappointment(request, id):
    updateinfo = Appointment.objects.get(id=id)
    formappointment = AppointmentForm(request.POST, instance=updateinfo)
    if formappointment.is_valid():
        formappointment.save()
        return redirect('/show')
    else:
        return render(request, 'editappointment.html')


def updateproduct(request, id):
    updateproduct = Product.objects.get(id=id)
    formproduct = ProductForm(request.POST, instance=updateproduct)
    if formproduct.is_valid():
        formproduct.save()
        return redirect('/show')
    else:
        return render(request, 'editappointment.html')


def updatecontact(request, id):
    updatecontact = Contact.objects.get(id=id)
    formcontact = ContactForm(request.POST, instance=updatecontact)
    if formcontact.is_valid():
        formcontact.save()
        return redirect('/show')
    else:
        return render(request, 'editcontacts.html')


def product(request):
    if request.method == "POST":
        myproducts = Product(
            name=request.POST['name'],
            price=request.POST['price'],
            quantity=request.POST['quantity']
        )
        myproducts.save()
        return redirect('/product')
    else:
        return render(request, 'product.html')


def register(request):
    if request.method == "POST":
        member = User(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

def upload_image(request):
    if request.method == "POST":
        form = ImagemodelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImagemodelForm()
    return render(request, 'upload_image.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


# Mpesa API views
def token(request):
    consumer_key = '6iCxJH6VLLKmCoHAAwEgql7tbOVHdPqb33bn1081EsaGYOYU'
    consumer_secret = 'P5bNmDnejA4aAMrkIIkO2xxTJrA0AKyAgHjH3tkxghXD6WUdM9t0FWUvgUWlpA5w'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
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
            "AccountReference": "Telemedicine",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment executed successfully")