from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("product/", views.product, name="Product"),
    path("currentproducts/", views.currentproducts, name="CurrentProducts"),
    path("editproduct/<int:myid>", views.editproduct, name="EditProduct"),
    path('deleteproduct/', views.deleteproduct, name='DeleteProduct'),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),

]
