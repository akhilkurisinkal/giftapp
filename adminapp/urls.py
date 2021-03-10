from django.urls import path
from . import views

urlpatterns = [
    path('paynow/<int:id>',views.paynow),
    path('payment/',views.payment),
    path('acustomerview/',views.acustomerview),
    path('asellerview/',views.asellerview),
    path('aorderview/',views.aorderview),
    path('ahome/',views.ahome),
    path('cardpayment/',views.cardpayment)
]
