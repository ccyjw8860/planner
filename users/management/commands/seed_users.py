from django_seed import Seed
from django.core.management.base import BaseCommand
from users.models import User
import random
import os

img_list = os.listdir('./uploads/user_photos')

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='how many users do you want to create')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            'email': lambda x: seeder.faker.email(),
            'nickname': lambda x: seeder.faker.name(),
            'photo': lambda x: f"user_photos/{random.choice(img_list)}"
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} of users are created!'))