from django.contrib import admin
from .models import User, Person, Bid, Listing, Comment

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Bid)
admin.site.register(Listing)
admin.site.register(Comment)

# Register your models here.
