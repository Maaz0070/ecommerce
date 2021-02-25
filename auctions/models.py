from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth import views


class User(AbstractUser):
    person = models.CharField(max_length=64)
    #bids = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="publisher")
    
    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    price = models.IntegerField() 
    num = models.IntegerField()
    #time = models.DateField()
    highestBidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner")

    def __str__(self):
        return f"${self.price}: with {self.num} bids and highest bidder is {self.highestBidder} with {self.time} remaining"

class Comment(models.Model):
    comment = models.CharField(max_length=64)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publisher")
    

    def __str__(self):
        return f"{self.publisher}: {self.comment} for {self.listing}"

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100000)
    image = models.URLField(max_length=2000)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    currentBid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="bid")
    comments = models.ManyToManyField(Comment, blank=True, related_name="post_comments")


    def __str__(self):
        return f"{self.title}: {self.description} by {self.seller} at {self.currentBid}"



