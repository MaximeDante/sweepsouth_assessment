
import requests
from django.core.management.base import BaseCommand
from products.models import Product


def get_products():
    url = 'https://fakestoreapi.com/products'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    products = r.json()
    return products


def seed_products():
    for i in get_products():
        product = Product(
            title=i["title"],
            price=i["price"],
            category=i["category"],
            description=i["description"],
            image=i["image"],
        )
        product.save()


def clear_data():
    Product.objects.all().delete()


class Command(BaseCommand):
    # Named (optional) arguments

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete data from the database',
        )
        parser.add_argument(
            '--seed',
            action='store_true',
            dest='seed',
            help='seed data into the database',
        )

    def handle(self, *args, **options):
        if options['delete']:
            clear_data()
            print("Data deleted")

        if options['seed']:
            seed_products()
            print("Seed Completed")
