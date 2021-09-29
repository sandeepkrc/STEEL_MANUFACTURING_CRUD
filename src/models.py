from django.db import models

class BussinessCustomer(models.Model):
    bcid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=200)
    cemail = models.EmailField(max_length=254)
    cadd = models.CharField(max_length=200)
    pwd = models.CharField(max_length=20)
    cpwd = models.CharField(max_length=20)




class Product(models.Model):
    id = models.IntegerField(primary_key=True)   #PRIMARY KEY USED
    pname= models.CharField(max_length=200)
    pcost = models.DecimalField(max_digits=10,decimal_places=4)
    pmfd = models.DateField(auto_now_add=True)
    quantity = models.CharField(max_length=225)
    def __str__(self):
        return self.pname

class Cart(models.Model):

    p = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart_id = models.AutoField(primary_key=True)
    b = models.ForeignKey(BussinessCustomer,on_delete=models.CASCADE) #user id from user table
    ctime = models.DateField(auto_now_add=True)
    price = models.IntegerField()   #total_price  means quantity  * one unit price# diff from pdt table
    quantity = models.IntegerField()


class Order(models.Model):

    order_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) #PRODUCT_ID   #ForeignKey USED
    bcid = models.IntegerField()   #ALSO WANT TO  RELATE WITH Bussiness TABLE#userid
    otime = models.DateField(auto_now_add=True)
    q = models.IntegerField()   #FOR Quantity
    p = models.IntegerField()  # FOR PRICE


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()