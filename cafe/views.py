from django.http.request import HttpRequest
from django.shortcuts import render,HttpResponse
from cafe.models import Contact, Order, Product, Rder
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    product = Product.objects.all()
    context = {'product':product}
    
    return render(request, 'product.html' ,context)
    
    


def contact(request):
    
    if request.method =="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        message =request.POST.get('message')
        contact= Contact(name=name, email=email, phone=phone ,message=message)
        contact.save()
    return render(request, 'contact.html')


def order(request):
    if request.method =="POST":
        ar =request.POST.get('ro')
        pr =request.POST.get('ao')
        sr =request.POST.get('so')
        
    return render(request, 'order.html' ,{'pr':pr ,'ar':ar ,'sr':sr})

def recipt(request):
    order = Order.objects.order_by('-oid')[:1]
    context = {'order':order}
    if request.method =="POST":
        oid =request.POST.get('oid')
        noc =request.POST.get('noc')
        cardno =request.POST.get('cardno')
        expiry =request.POST.get('expiry') 
        prod =request.POST.get('prod')
        price =request.POST.get('price')
        cvv =request.POST.get('cvv')
        street =request.POST.get('street')
        city =request.POST.get('city')
        state =request.POST.get('state')
        zip =request.POST.get('zip')
        order = Order(oid=oid,noc=noc ,cardno=cardno,expiry=expiry,prod=prod,price=price,cvv=cvv,street=street,city=city,state=state,zip=zip)
        order.save()
    return render(request, 'recipt.html',context)

