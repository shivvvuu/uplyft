from django.core.management.base import BaseCommand
from products.models import Product
from faker import Faker
import random

class Command(BaseCommand):
    help = "Populate the database with 100 fake products"

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = ['Electronics', 'Books', 'Clothing', 'Beauty', 'Home', 'Sports']

        for _ in range(100):
            Product.objects.create(
                name=fake.unique.company(),
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(10.00, 1000.00), 2),
                category=random.choice(categories)
            )
        self.stdout.write(self.style.SUCCESS("Successfully populated 100 products!"))
