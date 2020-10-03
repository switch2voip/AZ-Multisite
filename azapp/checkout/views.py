from django.shortcuts import render, redirect
from django.urls import reverse
import stripe

stripe.api_key = "sk_test_51HVFFsKH0Tn1qjaPiwYmgXmx5LStizCl7rFNOFdNJ7HA0G9YOKs4Yfv2EL7zjqc2VDLbsM7vWUOteW4gHGbCmVFY002CZ7VwgY"


# Create your views here.


def index(request):
    return render(request, 'checkout/checkout.html')


def charge(request):

    if request.method == 'POST':
        print('Date', request.POST)
        stripe.Customer.create(
            name=request.POST['name'],
            email=request.POST['email'],

        )

    return redirect(reverse('checkout/success'))


def success(request):

    return render(request, 'checkout/success.html')
