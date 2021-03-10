from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from adminapp.models import *

# Create your views here.
def paynow(request,id):
    return render(request,'payment.html',{'id':id})

def payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        exp = request.POST.get('exp')
        car = cards.objects.all()
        for i in car:
            if (i.name == name and i.cardnumber == cardnumber) and (i.cvv == int(cvv) and i.expdate == exp):
                print('name:',i.name)
                print(name)
                print('name:',i.cardnumber)
                print(cardnumber)
                print('name:',i.cvv)
                print('name:',cvv)
                print('name:',i.expdate)
                print('name:',exp)
                proid = request.POST.get('proid')
                item = products.objects.get(id=proid)
                remain = item.stock
                item.stock = remain-1
                item.save()
                lastorder = orders.objects.last()
                lastorder.cstatus = 'Order Accepted'
                lastorder.save()
                lastorder = orders.objects.last()
                '''log = customers.objects.last()
                email = log.email'''
                log = customerlogin.objects.last()
                custmerId = log.customerid
                row = login.objects.get(id=custmerId)
                username = row.username
                userrow = customers.objects.get(username=username)
                email = userrow.email
                subject = 'Order Details'
                m = ' Your Order Details '
                n = lastorder.customer
                o = 'Delivery Address:\t'+lastorder.caddress
                p = str(lastorder.ctime)+','+str(lastorder.cdate)
                q = 'Total amount paid:\t'+str(lastorder.camount)+' /- Rs'
                messagedupe = m+'\n\n'+'Dear\t'+n+','+'\n'+o+'\nDelivery Time & Date\t'+p+'\n'+q
                print(messagedupe)
                message = messagedupe
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'paymentmsg.html',{'msg':'Payment Success!!!!'})
            else:
                last = orders.objects.last()
                last.delete()
                return render(request,'paymentmsg.html',{'msg':'Payment Failed!!!!'})

def acustomerview(request):
    cus = customers.objects.all()
    lst = []
    for i in cus:
        lst.append(i)
    return render(request,'acustomerview.html',{'customers':lst})

def asellerview(request):
    sel = sellers.objects.all()
    lst = []
    for i in sel:
        lst.append(i)
    return render(request,'asellerview.html',{'sellers':lst})

def aorderview(request):
    tbl = orders.objects.all()
    lst = []
    for i in tbl:
        lst.append(i)
    return render(request,'aorderview.html',{'orders':lst})

def ahome(request):
    return render(request,'ahome.html')
    
def cardpayment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        exp = request.POST.get('exp')
        car = cards.objects.all()
        for i in car:
            if (i.name == name and i.cardnumber == cardnumber) and (i.cvv == int(cvv) and i.expdate == exp):
                log = customerlogin.objects.last()
                custmerId = log.customerid
                row = login.objects.get(id=custmerId)
                username = row.username
                userrow = customers.objects.get(username=username)
                email = userrow.email
                gift = giftcard.objects.last()
                validity = gift.validity
                amount = gift.amount
                code = gift.giftcode
                subject = 'Gift Card Details'
                m = ' Your Card Details '
                o = 'Redeem Code:\t'+str(code)
                p = str(validity)
                q = 'Total amount:\t'+str(amount)+' /- Rs'
                messagedupe = m+'\n\n'+'\n'+o+'\n Valid till:'+p+'\n'+q
                print(messagedupe)
                message = messagedupe
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'paymentmsg.html',{'msg':'Payment Success!!!!'})
            else:
                last = giftcard.objects.last()
                last.delete()
                return render(request,'paymentmsg.html',{'msg':'Payment Failed!!!!'})