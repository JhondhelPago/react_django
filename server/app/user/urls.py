from django.urls import path
from . import views



urlpatterns = [
    path('dev/', views.dev),
    path('dev2', views.dev2),
    path('show/users/', views.show_user),
    path('show/orders/', views.show_user_order_inner),
    path('show/orders/<int:user_id>', views.show_user_order_inner_by_user_id)
    
]