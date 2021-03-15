from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth import views


class User(AbstractUser):
    pass

    def __str__(self):
        return self.gamertag
    #bids = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="publisher")

class Person(models.Model):
    gamertag = models.CharField(max_length=64)
    passkey = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.gamertag} {self.passkey}"

class Bid(models.Model):
    price = models.IntegerField() 
    num = models.IntegerField()
    highestBidder = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"${self.price}: with {self.num} bids and highest bidder is [error]"

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.publisher}: {self.comment}"

class Listing(models.Model):
    title = models.CharField(max_length=50)
    businessMan = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=100000)
    image = models.URLField(max_length=2000)
    currentBid = models.ForeignKey(Bid, blank=True, null=True, on_delete=models.CASCADE, related_name="bid")
    comments = models.ForeignKey(Comment, blank=True, on_delete=models.CASCADE, related_name="post_comments")
    
    
    def __str__(self):
        return f"{self.title}: {self.description} by {self.seller} at {self.currentBid}"



