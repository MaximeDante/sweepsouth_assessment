import pytest
from products.models import Product
from products.serializers import ProductSerializer


@pytest.mark.django_db
class TestProductsView:
    def test_create_products(self, client) -> None:
        assert Product.objects.count() == 0
        response = client.post(
            '/products/', {
                'title': 'product 1',
                'price': 55,
                'category': 'category 1',
                'description': 'just a description',
                'image': 'https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg'
            }
        )
        assert response.status_code == 201, response.data
        assert Product.objects.count() == 1

    def test_list_products(self, client):
        assert Product.objects.count() == 0
        product = Product.objects.create(
            title='product 1',
            price=55,
            category='category 1',
            description='just a description',
            image='https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg'
        )

        response = client.get('/products/')
        assert response.status_code == 200
        assert response.json()['count'] == 1
        assert response.json()['results'][0] == {
            "id": product.id,
            'title': 'product 1',
            'price': '55.00',
            'category': 'category 1',
            'description': 'just a description',
            'image': 'https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg'
        }

    def test_get_product_detail(self, client):
        product = Product.objects.create(
            title='product 1',
            price=55.00,
            category='category 1',
            description='just a description',
            image='https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg'
        )

        response = client.get(f'/products/{product.id}/')
        assert response.status_code == 200
        json_string = {
            "id": product.id,
            'title': 'product 1',
            'price': '55.00',
            'category': 'category 1',
            'description': 'just a description',
            'image': 'https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg'
        }
        assert response.data == json_string

    def test_delete_product(self, client):
        product = Product.objects.create(
            title='product 1',
            price=55.00,
            category='category 1',
            description='just a description',
            image='https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg'
        )

        response = client.delete(f'/products/{product.id}/')
        assert response.status_code == 204


class TestProductsSerializer:
    def test_serialize_model(self):
        json_string = {
            "id": 1,
            'title': 'product 1',
            'price': '55.00',
            'category': 'category 1',
            'description': 'just a description',
            'image': 'https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg'
        }
        serializer = ProductSerializer(json_string)
        assert serializer.data
