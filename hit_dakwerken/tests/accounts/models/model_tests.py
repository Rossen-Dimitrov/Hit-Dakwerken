from django.contrib.auth import get_user_model
from django.test import TestCase
from hit_dakwerken.accounts.models import AppUser, AppUserProfile


class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='password123'
        )
        self.profile = AppUserProfile.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            company_name='Example Company'
        )

    def test_user_full_name(self):
        self.assertEqual(self.user.full_name, 'John Doe')

    def test_appuserprofile_user_relation(self):
        self.assertEqual(self.profile.user, self.user)

    def test_appuserprofile_default_values(self):
        profile = AppUserProfile.objects.create(
            user=get_user_model().objects.create_user(email='test2@example.com', password='password123')
        )
        self.assertIsNone(profile.first_name)
        self.assertIsNone(profile.last_name)
        self.assertIsNone(profile.company_name)
        self.assertIsNone(profile.company_url)
        self.assertIsNone(profile.company_address)

    def test_appuserprofile_created_on_auto_now_add(self):
        profile = AppUserProfile.objects.create(
            user=get_user_model().objects.create_user(email='test3@example.com', password='password123')
        )
        self.assertIsNotNone(profile.created_on)
