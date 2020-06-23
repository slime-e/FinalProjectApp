from django.test import TestCase
from .models import Dog, Breed, DogReview
from .views import index, getbreeds, getdogs
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import DogForm, BreedForm


class BreedTest(TestCase):
   def test_string(self):
       type=Breed(breedname="Weenie")
       self.assertEqual(str(type), type.breedname)

   def test_table(self):
       self.assertEqual(str(Breed._meta.db_table), 'breed')


class DogTest(TestCase):
   #set up one time sample data
   def setup(self):
       breed = Breed(breedname='Weenie')
       dog=Dog(dogname='bilbo', dogbreed=breed) #we know the true value is incalculable
       return dog
   def test_string(self):
       doggo=self.setup()
       self.assertEqual(str(doggo), doggo.dogname)

   def test_type(self):
       doggo=self.setup()
       self.assertEqual(str(doggo.dogbreed), 'Weenie')

   def test_table(self):
       self.assertEqual(str(Dog._meta.db_table), 'dog')


class ReviewTest(TestCase):
   def test_string(self):
       rev=DogReview(reviewtitle="Goodest Boy")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(DogReview._meta.db_table), 'dogreview')


class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetDogsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('dogs'))
       self.assertEqual(response.status_code, 200)


def setUp(self):
        self.u=User.objects.create(username='myuser')
        self.type=Breed.objects.create(breedname='weenie')
        self.woof = Dog.objects.create(dogname='bep', breed=self.kind, user=self.u, dogentrydate='2050-09-09', dogdescription="look at him")
        self.rev1=Review.objects.create(reviewtitle='superdogreview', reviewdate='2019-04-03', dog=self.dog, reviewrating=11, reviewtext='we cloned him')
        self.rev1.user.add(self.u)
        self.rev2=Review.objects.create(reviewtitle='dogtime', reviewdate='2020-05-21', dog=self.dog,  reviewrating=11, reviewtext='101 more')
        self.rev2.user.add(self.u)


def test_dog_detail_success(self):
        response = self.client.get(reverse('dog', args=(self.doggo.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)


class Breed_Form_Test(TestCase):
    def test_breedform_is_valid(self):
        form=BreedForm(data={'breedname': "type1", 'breeddescription' : "weenie"})
        self.assertTrue(form.is_valid())


    def test_breedform_empty(self):
        form=BreedForm(data={'breedname': ""})
        self.assertFalse(form.is_valid())


class New_Dog_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=Breed.objects.create(breedname='weenie')
        self.woof=Dog.objects.create(dogname='bilbo', dogbreed=self.type, user=self.test_user, dogvalue=500000, dogentrydate='2019-04-02', dogurl= 'someplaceorother', dogdescription="a doggo")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newdog'))
        self.assertRedirects(response, '/accounts/login/?next=/finalapp/newDog/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newdog'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finalapp/newdog.html')
        