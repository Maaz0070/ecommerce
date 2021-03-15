from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User, Listing, Person, Comment, Bid


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
        username = User()
    else: #if user didnt just fill form they need to go to login page to do that
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST": #if they just filled out register form
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        #save person in Person model
        """
        person = Person()
        person.gamertag = username
        person.passkey = password
        person.save()
        """

        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user) #logs in user 
        return HttpResponseRedirect(reverse("index")) #takes to index
    else:
        return render(request, "auctions/register.html") #if they click register

@login_required
def newListing(request):
    if request.method == "POST": #if they just enetered values for new listing
        title = request.POST["title"]
        description = request.POST["description"]
        bid = request.POST["bid"]
        image = request.POST["photo"]
        category = request.POST["category"]
        #maybe you still need to create a user somehow

        comments = Comment()
        comments.comment = "Leave any comments below and ill reply"
        comments.publisher = User.username
        comments.save()

        initialBid = Bid()
        initialBid.price = bid
        initialBid.num = 1
        initialBid.highestBidder = User.username
        initialBid.save()

        product = Listing()
        product.title = title
        product.category = category
        product.description = description
        product.businessMan = User.username
        product.currentBid = initialBid
        product.comments = comments
        product.image = image
        product.category = category
        product.save()
    
    return render(request, "auctions/new.html") #right when they cllick the button

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing.html", {
        "title": title,
        "description": description,
        "image": image,
        "seller": seller,
        "bid": currentBid
    })
