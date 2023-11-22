from django.http import HttpResponse
from django.shortcuts import render
from shop_side.models import Product, Category

def est_li_tsifra(str):
    for i in str:
        if i.isdigit():
            return True

def est_li_bukva(num):
    for i in num:
        if i.isalpha():
            return True

def product_create_view(request):
    context = {'category_list': Category.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        if est_li_tsifra(name):
            return HttpResponse(''' <script>
                                        alert('Invalid')
                                    </script> ''')
        elif est_li_bukva(price):
            return HttpResponse(''' <script>
                                        alert('Invalid')
                                    </script> ''')
        elif est_li_bukva(quantity):
            return HttpResponse(''' <script>
                                        alert('Invalid')
                                    </script> ''')
        elif not category.isdigit() or int(category) > len(Category.objects.all()) or int(category) < 0:
            return HttpResponse(''' <script>
                                        alert('Invalid')
                                        window.location.href = "//127.0.0.1:8000"
                                    </script> ''')
        else:
            product = Product()
            product.name = name
            product.price = price
            product.quantity = quantity
            product.category = Category.objects.get(
                pk=category
            )

            product.save()

    return render(request,
                  'shop_side/product_create.html',
                  context)


