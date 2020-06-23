from django.db import models
from django.contrib.auth.models import User


class Breed(models.Model):
    breedname=models.CharField(max_length=50)
    breeddescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.breedname
    
    class Meta:
        db_table='breed'
        verbose_name_plural='breeds'


class Dog(models.Model):
    dogname=models.CharField(max_length=255)
    dogbreed=models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dogmass=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dogvalue=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    dogentrydate=models.DateField()
    dogurl=models.URLField(null=True, blank=True) #add image support or just link to an image
    dogdescription=models.TextField()

#deleted any discount functions
    def __str__(self):
        return self.dogname
    
    class Meta:
        db_table='dog'
        verbose_name_plural='dogs'


class DogReview(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    dog=models.ForeignKey(Dog, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='dogreview'
        verbose_name_plural='dogreviews'