from django.core.management.base import BaseCommand
from Userapp.models import ShopUser, ShopUserProfile

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = ShopUser.objects.all()
        for user in users:
            user_profile = ShopUserProfile.objects.create(user=user)
            user_profile.save()
            