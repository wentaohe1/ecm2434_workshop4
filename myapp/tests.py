from django.test import TestCase
from django.urls import reverse
from myapp.models import Item
from myapp.forms import ItemForm

class ItemModelTest(TestCase):
    def test_create_item(self):
        """Test creating an Item instance"""
        item = Item.objects.create(name="Laptop", price=999.99)
        self.assertEqual(item.name, "Laptop")
        self.assertEqual(item.price, 999.99)

class ItemViewTest(TestCase):
    def test_homepage_loads(self):
        """Test if the homepage loads successfully"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class ItemFormTest(TestCase):
    def test_valid_form(self):
        """Test if the form is valid"""
        form_data = {'name': 'Phone', 'price': 499.99}
        form = ItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if an invalid form is rejected"""
        form_data = {'name': '', 'price': -100}
        form = ItemForm(data=form_data)
        self.assertFalse(form.is_valid())
