from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

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

    # orderlist = serialize(
            
    #         'json',
    #         order.objects.select_related('user').all(),
    #         use_natural_foreign_keys=True    

    #     )


    orderlist = list(
        order.objects.select_related('user').all().values(
            'id', 'product', 'user', 'user__id', 'user__username', 'user__age', 'user__gender', 'user__email', 'user__password'
        )
    )

    return JsonResponse(orderlist, safe=False)


def show_user_order_inner_by_user_id(req, user_id):


    try:

        orderlist = list(
                order.objects.select_related('user').filter(user_id=user_id).values(
                    'id', 'product', 'user', 'user__id', 'user__username', 'user__age', 'user__gender', 'user__email', 'user__password'
                )
            )
        
        return JsonResponse(orderlist, safe=False)
    except Exception as e:

        print(F"error @ show_user_order_inner_by_user_id, {e}")









    # orderlist = order.objects.select_related('user').get(order.user)


