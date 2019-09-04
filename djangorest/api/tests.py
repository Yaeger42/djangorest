from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core import reverse
from .models import BucketList
from django.contrib.auth.models import User
# Create your tests here.
class ModelTestCase(TestCase):
    #This class defines the test suite for the bucketlist model"
    
    def setUp(self):
        #Define the test client and other test variables
        user = User.objects.create(username = "nerd")
        self.name = "Write world class code"
        self.bucketlist_name = "Write world class code"
        self.bucketlist = BucketList(name = self.name, owner = user) #THIS HAS BEEN CHANGED

    def test_model_can_create_a_bucketlist(self):
        #Test the bucketlist model can create a bucketlist
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    #Test suite for the api views

    def setUp(self):
        #define the test client and other test variables
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format ="json")

    def test_api_can_create_a_bucketList(self):
        #Test the api has bucket creation capability
        self.assertEqual(self.responde.status_code, status.HTTP_201_CREATED)
    
    #Test the api can get a bucket list

    def test_api_can_get_a_bucketlist(self):
        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs = {'pk': bucketlist.id}), format = "json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        #Test the api can update a given bucketlist
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs = {'pk': bucketlist.id}),
            change_bucketlist, format = "json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        #Api can delete a bucketlist
        bucketlist = BucketList.objects.get()
        response = self.client.delete(
            reverse('details', kwars= {'pk': bucketlist.id}),
            format = "json",
            follow = True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class ViewTestCase(TestCase):
    #Test suite for the API views
    def setUp(self):
        #Define the test client and other test variables
        user = User.objects.create(user = user)
        #Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user = user)
        #User model it's not serializable, so we use the ID/PK
        self.bucketlist_data = {'name': 'Go to ibiza', 'owner':user.id}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format = "json"
        )

    def test_api_can_create_a_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get('/bucketlists', kwargs = {'pk': 3}, format = "json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_api_can_get_a_bucketlist(self):
        #Test the api can get a given bucketlist based on a user
        #We post a user and if evertything is okay, we get a nice 200 HTTP response
        bucketlist = BucketList.objects.get(id = 1)
        response= self.client.get(
            '/bucketlists/',
            kwargs = {'pk': bucketlist.id}, format = "json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist) #La respuesta HTTP contiene la respuesta DUH y el bucketlist

    def test_api_can_update_bucketlist(self):
        #Test the api can update a given bucketlist
        bucketlist = BucketList.objects.get()
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs = {'pk': bucketlist.id}),
            change_bucketlist, format = "json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        #API can delete bucketlist
        BucketList = BucketList.object.get()
        response = self.client.delete(
            reverse('details', kwargs = {'pk': bucketlist.id}),
            format = "json",
            follow = True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    