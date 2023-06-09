from django.shortcuts import render,redirect
from django.http import HttpResponse
from carts.models import CartItem,Cart
from .forms import OrderForm
from .models import Order,OrderProduct,Payment
import datetime
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from eachcategorypages.models import Product
# Create your views here.
@login_required(login_url='login')
def payment(request):
    
    order=Order.objects.get(user=request.user,is_ordered=False)
    payment=Payment(
        user=request.user,
        
    )
    
    
    return render(request,'order_show.html')




@login_required(login_url='login')
def place_order(request,total=0,quantity=0):
    current_user=request.user

    #if the cart count is lessthan or equal to zero ,then redirect to home
    cart_items=CartItem.objects.filter(user=current_user)
    cart_count=cart_items.count()
    if cart_count<=0:
        return redirect('home')
    
    total=0
    for cart_item in cart_items:
        total+=(cart_item.product.price * cart_item.quantity)
        quantity+=cart_item.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #store all the order iinformation inside the order table
            data = Order()
            
            data.user = current_user

            data.first_name=form.cleaned_data['first_name']

            data.last_name=form.cleaned_data['last_name']

            data.phone_name=form.cleaned_data['phone']

            data.email_name=form.cleaned_data['email']
            
            data.address_line_1=form.cleaned_data['address_line_1']
            
            data.address_line_2=form.cleaned_data['address_line_2']

            data.country=form.cleaned_data['country']

            data.state=form.cleaned_data['state']

            data.city=form.cleaned_data['city']

            data.order_note=form.cleaned_data['order_note']

            data.order_total= total

        
            data.ip = request.META.get('REMOTE_ADDR')

            data.save()

            #generate order number

            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()


            return redirect('checkout')
        else:
            return redirect('checkout')
   
    
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart    



@login_required(login_url='login')
def order_show(request,total=0,quantity=0,cart_items=None):

        cart=Cart.objects.get(cart_id=_cart_id(request))
        
        cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        
        order =Order.objects.filter(user=request.user).last()
        context={
             'order':order,
            'cart_items':cart_items,
            }

        return render(request,'order_show.html',context)
    
    
    
    

def remove_cart_item(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.filter(product=product,cart=cart)
    
    cart_item.delete()
    return redirect('cart')

    