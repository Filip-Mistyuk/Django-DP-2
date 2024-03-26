from django.shortcuts import render, redirect
from .models import Product, Review
from .forms import ReviewForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'hzchto/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = Review.objects.filter(product=product)
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        rating = request.POST['rating']
        review = Review.objects.create(product=product, author=author, text=text, rating=rating)
        return redirect('product_detail', product_id=product_id)
    return render(request, 'hzchto/product_detail.html', {'product': product, 'reviews': reviews})

def add_review(request, product_id):
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        rating = request.POST['rating']
        review = Review.objects.create(product_id=product_id, author=author, text=text, rating=rating)
    return redirect('product_detail', product_id=product_id)