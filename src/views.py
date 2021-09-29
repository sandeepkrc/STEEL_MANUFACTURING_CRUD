from django.shortcuts import render,redirect
from .models import Product,BussinessCustomer,Order,Cart,Contact
from django.http import HttpResponse
import logging
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib import messages

########################### FOR DB LOGGER   #################
# db_logger = logging.getLogger('db')
# # db_logger = logging.getLogger('db')
# db_logger.info('info message')
# db_logger.warning('warning message')

# try:
#     1/0
# except Exception as e:
#     db_logger.exception(e)
 ############################### #############################

# FOR SHOWING ALL OPTIONS
def contact(request):
    return render(request,"c.html")

def test(request):
    return render(request,"c.html")
class Home(View):
    def post(self,request):
        pass


    def get(self,request):
        print("----")
        if 'user' in request.session:
            current_user = request.session['user']
            # product_list = Product.objects.all()
            return render(request, "index.html",{"current_user":current_user})
            # return render(request,"order.html",{"product":product_list,"current_user":current_user})

        else:
            return render(request,"index.html")




            # return HttpResponse("HOME VIEW WITHOUT LOG IN")






# FOR REGISTERING PRODUCT

class Register_Product(View):
    def post(self,request):
        dict1 ={}
        dict1[1] = request.POST["id"]
        dict1[2] = request.POST.get("name")
        dict1[3] = request.POST.get("cost")
        dict1[4]= request.POST.get("qty")
        print(dict1)
        obj = Product(id=dict1[1], pname=dict1[2], pcost=dict1[3],quantity=dict1[4])
        obj.save()
        return render(request,'padded.html')
    def get(self,request):
        return render(request, 'pregister.html')

# FOR REGISTERING BUSSINESS CUSTOMER

class Register_Bcustmer(View):

    # if request.method == "POST":
    def post(self,request):

        dict1 ={}
        dict1[1] = request.POST['bcid']
        dict1[2] = request.POST['cname']
        dict1[3] = request.POST['email']
        dict1[4] = request.POST['add']
        dict1[5] = request.POST['p']
        dict1[6] = request.POST['c']
        print(dict1)
        bcid = request.POST['bcid']
        name = request.POST['cname']



        #    WRITE THE LOGIC  FOR FILTER DUPLICATE USERNAME

        # u= BussinessCustomer.objects.filter(cname= name)
        # if u:

        email = request.POST['email']
        add = request.POST['add']
        pwd1 = request.POST['p']
        pwd2 = request.POST['c']

        #  IF PASSWORD MATCH

        if pwd1==pwd2:
            obj = BussinessCustomer(bcid= bcid,cname=name ,cemail=email,cadd=add,pwd=pwd1,cpwd=pwd2)
            obj.save()
            return render(request,"login.html",{"rs": "Registration successful!! Please "})
        else:
            context ={'msg' :"Password and Confirm Password should be same-","try":"Try again!!"}
            return render(request,"bregister.html",context)

    def get(self,request):
        context= {"f": "Welcome to Registration "}
        print("geet")
        return render(request, 'bregister.html',context)

##  FOR LOGIN BUSSINESS Customer

class Login_Bcustomer(View):
    def post(self,request):
        username = request.POST['un']
        pwd = request.POST['pw']
        qs= BussinessCustomer.objects.filter(cname= username,pwd=pwd)

        if qs:

            request.session['user'] = username
            current_user = request.session['user']
            return render(request,"successl.html",{"current_user":current_user})
                #login success html page
        else:
            context= {"msg": " Failed !! Invalid credentials Try again"}
            return render(request,"login.html",context)
    def get(self,request):
        return render(request,'login.html')





def logout(request):

    try:
        del request.session['user']


    except KeyError:

        return render(request,"login.html",{"msg": "First to Logout"})

    return render(request, "logout.html")







class User_Detail(View):
    def get(self,request):
        id = request.POST["bcid"]
        usr = BussinessCustomer.objects.filter(bcid=id)
        pass


## FOR  SHOWING ALL PRODUCT ORDER
#
class View_Product(View):
    def get(self,request):
        product_list = Product.objects.all()
        if 'user' in request.session:
            current_user = request.session['user']
            return render(request,'order.html',{"product":product_list,"current_user":current_user})
        else:
            return render(request, 'order.html', {"product": product_list})



class Add_To_Cart(View):
    def post(self,request):
        pass
    def get(self,request):
        var = request.GET["pid"]
        c = request.GET["custu"]

        cart_qs = Cart.objects.filter(p_id=var)
        product_qs = Product.objects.filter(id=var)
        print(cart_qs)
        if cart_qs:
            # UPDATE PRODUCT IN CART
            for p in cart_qs:
                newqty = p.quantity
                newqty +=1

                for pc in product_qs:
                    new_price = p.price + pc.pcost

                obj= Cart.objects.filter(p_id=var).update(quantity=newqty,price=new_price)#
                # value added to the cart list
                return redirect("/Cart_View")
        else:
            #  NOT IN CART
            product_qs = Product.objects.filter(id=var)
            for a in product_qs:
                print("product id is", var)
                print("PRICE ",a.pcost)

            customer_id = c
            one=1
            cost=one*(a.pcost)
            obj = Cart(price=cost,b_id=customer_id,p_id=var,quantity=one)
            obj.save()
            print("save data in cart")

        return redirect("/Cart_View")

        # return render(request,"show_cart.html")



class Cart_View(View):
    def get(self,request):
        object = Cart.objects.all()
        # print(obj.price)
        return render(request,"show_cart.html",{"obj":object})




#  LOGIC FOR BUYING PRODUCT

class Order_Product(View):
    def post(self,request):
        cid = request.POST["cid"]
        obj_cart = Cart.objects.filter(cart_id=cid)
        for i in obj_cart:
            var1=i.b_id
            var2=i.p_id
            var3=i.quantity
            var4=i.price
            var = i.cart_id
            order_obj = Order(order_id=var,bcid=var1,q=var3,p=var4,product_id=var2)
            order_obj.save()


            # WRITE LOGGIC FOR DELETE FRTOM CART


            del_cart= obj_cart.delete()
            print(" DELETE from cart")
        return render(request,"orderedsuccess.html")
















# def product_delete(request,p_id):
#     d= Product.objects.get(id=p_id)
#     d.delete()
#     return redirect(order_product)

class Product_Delete(View):
    def post(self,request):
        if 'user' in request.session:
            current_user = request.session['user']
            try:
                did = request.POST["pid"]
                d= Product.objects.filter(id=did)
                if d:
                    d.delete()
                    product_list = Product.objects.all()
                    return render(request,'order.html',{"product":product_list,"delete":"Product deleted successfully"})
                else:
                    return render(request,"delete.html",{"msg":"Please Enter Valid Product ID","current_user":current_user})
            except:
                return render(request,"delete.html",{"msg":"Please Entr Numeric Value","current_user":current_user})
        else:
            return redirect("login_bcustomer")



    def get(self,request):
        if 'user' in request.session:
            current_user = request.session['user']
            return render(request,"delete.html",{"msg":"Delete Product by Product ID ","current_user":current_user})
        else:
            return redirect("login_bcustomer")

class Update_Product(View):
    def get(self,request,pid):
        update_product = Product.objects.get(id=pid)
        return render(request,"update.html",{"up": update_product})
    def post(self,request,pid):

        update_product = Product.objects.get(id=pid)
        ncost = request.POST["cost"]
        nqty = request.POST["qty"]
        obj= Product.objects.filter(id=pid).update(pcost=ncost,quantity=nqty)
        product_list = Product.objects.all()
        return render(request,'order.html',{"product":product_list,"msg":"PRODUCT UPDATED !!!"})

def payment(request):
    if request.method =="POST":
        name= request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        email = request.POST.get("email")
        client = razorpay.Client(auth =("rzp_test_rD0wv59lvmLapP","ajYc8euRPGfd31WCxgmP8NZN"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        coffe = Coffe(name=name,amount=amount,email=email,payment_id = payment['id'],)
        coffe.save()
        return render(request,'payment.html',{'payment':payment})
    return render(request,"payment.html")
########################## UNDER WORKING      W  O   P
# def ordered(request):
#     if request.method=="POST":
#         pid = request.POST["pid"]
#         qty = request.POST["qty"]
#         qtyi=int(qty)
#         obj = Product.objects.get(id=pid)
#         print("----",obj)
#
#         return render(request,"osuccess.html")
#     # o = Order.objects.get(product_id=o_id)
#     return render(request,"osuccess.html")

# def ordered(request,oid):
#     # print(oid)
#     if request.method=="POST":
#         newc = request.POST["ncost"]
#         print(newc)
#         u= Product.objects.filter(id=oid).update(pcost=newc)
#         return redirect('order_product')
#     return render(request,"uinput.html")



# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import User
#
#
# # Create your views here.
# def home(request):
#     if 'user' in request.session:
#         current_user = request.session['user']
#         param = {'current_user': current_user}
#         return render(request, 'base.html', param)
#     else:
#         return redirect('login')
#     return render(request, 'login.html')
#
#
#
# def signup(request):
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         pwd = request.POST.get('pwd')
#         # print(uname, pwd)
#         if User.objects.filter(username=uname).count()>0:
#             return HttpResponse('Username already exists.')
#         else:
#             user = User(username=uname, password=pwd)
#             user.save()
#             return redirect('login')
#     else:
#         return render(request, 'signup.html')
#
#
#
# def login(request):
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         pwd = request.POST.get('pwd')
#
#         check_user = User.objects.filter(username=uname, password=pwd)
#         if check_user:
#             request.session['user'] = uname
#             return redirect('home')
#         else:
#             return HttpResponse('Please enter valid Username or Password.')
#
#     return render(request, 'login.html')
#
#
# def logout(request):
#     try:
#         del request.session['user']
#     except:
#         return redirect('login')
#     return redirect('login')




# <!DOCTYPE html>
# <html>
# <head>
#     <title>{% block title %}{% endblock %}</title>
# </head>
# <body>
#     <h1>My Site</h1>
#
#     <a href="/">Home</a>
#     <span>/</span>
#
#     {% if current_user %}
#         <a href="{% url 'logout' %}">Logout</a>
#         <hr>
#         <h2>Welcome <span style="color: dodgerblue;">{{current_user}}</span>!</h2>
#     {% else %}
#         <a href="{% url 'login' %}">Login</a>
#         <span>/</span>
#         <a href="{% url 'signup' %}">Sign Up</a>
#         <hr>
#         <h2>Login to access this website!</h2>
#     {% endif %}
#
#
#     {% block body %}{% endblock %}
# </body>
# </html>
# 2. create login.html
# {% extends 'base.html' %}
# {% block title %}Login{% endblock %}
#
# {% block body %}
#     <h2>Login</h2>
#
#     <form method="POST">
#         {% csrf_token %}
#         <input type="text" name="uname" placeholder="User Name">
#         <br><br>
#         <input type="text" name="pwd" placeholder="Password">
#         <br><br>
#         <input type="submit" name="submit" value="Login">
#     </form>
#
#
# {% endblock %}
# 3. create signup.html
# {% extends 'base.html' %}
# {% block title %}Sing Up{% endblock %}
#
# {% block body %}
#     <h2>Sign Up</h2>
#
#     <form method="POST">
#         {% csrf_token %}
#         <input type="text" name="uname" placeholder="Username">
#         <br><br>
#         <input type="text" name="pwd" placeholder="Password">
#         <br><br>
#         <input type="submit" name="submit" value="Sign Up">
#     </form>
#
# {% endblock %}
