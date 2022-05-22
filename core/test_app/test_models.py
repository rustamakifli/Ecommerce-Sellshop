from django.test import TestCase
from core.models import Contact

class ContactTest(TestCase):
    
    def setUp(self):
        self.data = {
            "name" : "TestName",
            "email" : "Test@email.com"
        }
        self.contact = Contact.objects.create(**self.data)

    def test_model_data(self):
        self.assertEqual(self.data["name"], self.contact.name)

    def test_str_method (self):
        self.assertEqual(str(self.contact), self.data["name"])

    def tearDown(self): #the test runner will invoke that method after each test and tearDown deletes contact object.
        del self.contact

