from django.shortcuts import render
from .models import Dog, Breed, DogReview
from .forms import DogForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def index (request):
    return render(request, 'finalapp/index2.html')


def getbreeds(request):
    breed_list=Breed.objects.all()
    return render(request, 'finalapp/breeds.html', {'breed_list' : breed_list})


def getdogs(request):
    dogs_list=Dog.objects.all()
    return render(request, 'finalapp/dogs.html', {'dogs_list': dogs_list})


def dogdetails(request, id):
    woof=get_object_or_404(Dog, pk=id)
    reviews=DogReview.objects.filter(dog=id).count()
    context={
        'woof' : woof,
        'reviews' : reviews,
    }
    return render(request, 'finalapp/dogdetails.html', context=context)


@login_required
def newDog(request):
     form=DogForm
     if request.method=='POST':
          form=DogForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=DogForm()
     else:
          form=DogForm()
     return render(request, 'finalapp/newdog.html', {'form': form})


def loginmessage(request):
    return render(request, 'finalapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'finalapp/logoutmessage.html')