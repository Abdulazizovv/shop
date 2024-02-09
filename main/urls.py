from django.urls import path
from .views import index, products, sold_products, handle_selected_products, add_product, warehouse, edit_product, delete_product


urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('getdata/', handle_selected_products, name='getdata'),
    path('sold-products/', sold_products, name='sold'),
    path('add-product/', add_product, name='add_product'),
    path('warehouse/', warehouse, name='warehouse'),
    path('edit-product/', edit_product, name="edit_product"),
    path('delete-product/<int:product_id>/', delete_product, name="delete")
]