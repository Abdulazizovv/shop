from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Warehouse, Category, SoldProduct
from django.http import JsonResponse
import json
from django.contrib import messages


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})
    

def products(request):
    products = Warehouse.objects.filter(is_available=True).order_by('-arrived')
    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products, 'categories':categories})



def sold_products(request):
    sold_products = SoldProduct.objects.all().order_by("-sold_time")
    return render(request, "sold_products.html", {'sold_products': sold_products})


def warehouse(request):
    products = Warehouse.objects.all().order_by("-arrived")
    categories = Category.objects.all()
    return render(request, "warehouse.html", {'products':products, 'categories':categories})


def handle_selected_products(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        products = data.get('products')
        quantities = data.get('quantities')
        print(quantities)
        for product in quantities:
            ware = get_object_or_404(Warehouse, id=product["productId"])
            quantity = int(product["quantity"])
            if quantity <= ware.quantity:
                ware.quantity -= quantity
                ware.save()
                SoldProduct(product=ware, quantity=quantity).save()
               
        messages.success(request, "Muvaffaqqiyatli sotildi!")
        return JsonResponse({'message': 'Data received successfully'}, status=200)
    else:
        messages.error(request, "Nimadir xato ketdi qaytadan urining!")
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    

def add_product(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        new_category = request.POST.get("newCategory")
        
        if category_id == 'new':
            category = Category.objects.create(title=new_category)
        else:
            category = Category.objects.get(id=category_id)
        
        quantity = request.POST.get("quantity")
        image = request.FILES.get("image")
        description = request.POST.get("description")
        if image:
            product = Product.objects.create(
                title=title,
                price=price,
                category=category,
                image=image,
                description=description
            )
        else:
            product = Product.objects.create(
                title=title,
                price=price,
                category=category,
                description=description
            )

        Warehouse.objects.create(
            product=product,
            quantity=quantity
        )

        redirect_url = request.POST.get("redirect_url")
        return redirect(redirect_url)
    

def edit_product(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        new_category = request.POST.get("newCategory")
        print(request.POST.get("product_id"))
        
        if category_id == 'new':
            category = Category.objects.create(title=new_category)
        else:
            category = Category.objects.get(id=category_id)
        
        quantity = request.POST.get("quantity")
        image = request.FILES.get("image")
        description = request.POST.get("description")
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        product.title = title
        product.description = description
        product.category = category
        product.price = price
        if image:
            product.image = image
        product.save()
        warehouse = get_object_or_404(Warehouse, product=product)
        warehouse.quantity = quantity
        warehouse.save()
        messages.success(request, "Product has been changed!")

        redirect_url = request.POST.get("redirect_url")
        return redirect(redirect_url)


def delete_product(request, product_id):
    product = get_object_or_404(Warehouse, id=product_id)
    product.delete()
    return redirect("warehouse")