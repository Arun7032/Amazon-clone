from django.shortcuts import render

# Create your views here.
def amazon_home(request):
    return render(request, 'amazon_home.html')

def fresh(request):
    return render(request, 'fresh.html')

def seller(request):
    return render(request, 'seller.html')

def best_seller(request):
    return render(request, 'best_seller.html')

def mobiles(request):
    return render(request, 'mobiles.html')

def todays_deals(request):
    return render(request, 'todays_deals.html')
 
def customer_service(request):
    return render(request, 'customer_service.html')

def new_releases(request):
    return render(request, 'new_releases.html')

def prime(request):
    return render(request, 'prime.html')

def fashion(request):
    return render(request, 'fashion.html')

def amazon_pay(request):
    return render(request, 'amazon_pay.html')

def electronics(request):
    return render(request, 'electronics.html')

def homeAndKitchen(request):
    return render(request, 'home&kitchen.html')

def computers(request):
    return render(request, 'computers.html')

def books(request):
    return render(request, 'books.html')

def gift_cards(request):
    return render(request, 'gift_cards.html')
