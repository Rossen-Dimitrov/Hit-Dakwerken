from django.test import TestCase
from hit_dakwerken.accounts.forms import AppUserRegisterForm, AppUserEditForm


class TestForms(TestCase):
    def test_app_user_register_form_valid_data(self):
        form = AppUserRegisterForm(data={
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertTrue(form.is_valid())

    def test_app_user_register_form_invalid_data(self):
        form = AppUserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Email, password1, and password2 are required

    def test_app_user_edit_form_valid_data(self):
        form = AppUserEditForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'company_name': 'Example Company',
            'company_address': '123 Example St',
            'company_url': 'https://example.com'
        })
        self.assertTrue(form.is_valid())

    def test_app_user_edit_form_invalid_data(self):
        form = AppUserEditForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)  # All fields are required
