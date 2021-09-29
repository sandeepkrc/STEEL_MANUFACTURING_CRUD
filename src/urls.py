from django.urls import path
from src import views

urlpatterns = [
    path("AA",views.test),
    path("contact",views.contact,name="contact"),

    path('', views.Home.as_view(), name='home'),
    path('view_product',views.View_Product.as_view(),name = 'view_product'),
    path('register_product',views.Register_Product.as_view(),name = 'register_product'),
    path('register_bcustomer',views.Register_Bcustmer.as_view(),name = 'register_bcustomer'),
    path('login_bcustomer',views.Login_Bcustomer.as_view(),name = 'login_bcustomer'),


    path("delete_product",views.Product_Delete.as_view(),name="product_delete"),
    path("update_product/<int:pid>/",views.Update_Product.as_view(),name="update_product"),
    path("add_to_cart",views.Add_To_Cart.as_view(),name="add_to_cart"),
    path("Cart_View",views.Cart_View.as_view(),name="Cart_View"),

    path("order_product",views.Order_Product.as_view(),name="order_product"),
    path("payment",views.payment,name="payment"),


    path("logout",views.logout,name="logout"),






    # path("ordered_product",views.ordered,name="ordered_p"),

    # path("o/<int:ord_id>/",views.ord,name="ord"),
    # path("o/<int:ord_id>/",views.ord,name="ord"),

    # path("order",views.)

]
