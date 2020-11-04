from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [

    path('', views.home, name='home'),

    path('marketplace/', views.placements, name='placements'),
    path('marketplace/<placement_slug>/', views.placement_detail, name='placement-detail'),

    path('my-bids/', views.bid_summary, name='bid-summary'),
    path('confirm-bids/', views.confirm_bids, name='confirm-bids'),

    path('about/', views.about, name='about')
]
