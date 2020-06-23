from django.contrib import admin
from .models import Dog, Breed, DogReview


# Register your models here.
admin.site.register(Dog)
admin.site.register(Breed)
admin.site.register(DogReview)