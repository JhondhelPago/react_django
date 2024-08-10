from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
#function to fire up

def dev(req):

    data ={
        "developer_name" : 'Jhondhel Pago',
        "developer_email" : 'jhondhelpago2307@gmail.com',
    }

    return JsonResponse(data, safe=False)