from django.shortcuts import render
from django.http import JsonResponse

#models imports
from django.contrib.auth.models import User
from .models import user, order



# Create your views here.
#function to fire up

def dev(req):

    data ={
        "developer_name" : 'Jhondhel Pago',
        "developer_email" : 'jhondhelpago2307@gmail.com',
    }

    return JsonResponse(data, safe=False)


def dev2(req):

    data = {
        "developer_name" : 'Jhondhel Pago',
        "developer_email" : 'pago.j.bscs@gmail.com',
    }

    return JsonResponse(data, safe=False)


def show_user(req):

    Users = list(User.objects.all().values())

    return JsonResponse(Users, safe=False)

def show_user_order_inner(req):

    orders = list(order.objects.select_related('user').all())


    return JsonResponse(orders, safe=False)


