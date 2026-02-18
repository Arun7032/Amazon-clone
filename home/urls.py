from django.urls import path
from . import views

urlpatterns = [
    path('', views.amazon_home, name='amazon_home'),
    path('fresh/', views.fresh, name='fresh'),
    path('seller/', views.seller, name='seller'),
    path('best_seller/', views.best_seller, name='best_seller'),
    path('mobiles/', views.mobiles, name='mobiles'),
    path('todays_deals/', views.todays_deals, name='todays_deals'),
    path('customer_service/', views.customer_service, name='customer_service'),
    path('new_releases/', views.new_releases, name='new_releases'),
    path('prime/', views.prime, name='prime'),
    path('fashion/', views.fashion, name='fashion'),
    path('amazon_pay/', views.amazon_pay, name='amazon_pay'),
    path('electronics/', views.electronics, name='electronics'),
    path('home&kitchen/', views.homeAndKitchen, name='home&kitchen'),
    path('computers/', views.computers, name='computers'),
    path('books/', views.books, name='books'),
    path('gift_cards/', views.gift_cards, name='gift_cards'),


]
