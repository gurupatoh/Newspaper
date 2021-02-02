from django.db import models
from django.contrib.auth import get_user_model


class Placement(models.Model):
    # A placement allows users  to bid on jobs
    placement_title = models.CharField(max_length=250)
    placement_slug = models.SlugField()


placement_created = models.DateTimeField(auto_now_add=True)
placement_modified = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.placement_title


class Bid(models.Model):
    """
    The bid, same with 'order'
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bid_status = models.BooleanField(default=False)

    bid_created = models.DateTimeField(auto_now_add=True)
    bid_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} -{}'.format(self.user, self.bid_status)


class PlacementBid(models.Model):
    """
    The junction table for placement and bid models/tables. Contains every instance of a bid for a placement
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)

    offer = models.IntegerField()
    shares = models.IntegerField()
    confirmed = models.BooleanField(default=False)

    placement_bid_created = models.DateTimeField(auto_now_add=True)
    placement_bid_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['placement_bid_modified']

    def __str__(self):
        return '{} - {} - {}'.format(self.shares, self.offer, self.user)
