from django.contrib import admin
from .models import Placement, PlacementBid, Bid

# Register your models here.
admin.site.register(Placement)
admin.site.register(PlacementBid)
admin.site.register(Bid)
