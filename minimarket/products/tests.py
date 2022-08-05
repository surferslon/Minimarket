from timeit import default_timer as timer

from django.test import TestCase
from products.models import Category, Product
from rest_framework import status
from rest_framework.test import APIClient

TEST_PRODUCT_PRICE = 15.15
TEST_PRODUCT_COUNT = 42
TEST_PRODUCT_ITEMS = 10_000
MAX_RESPONSE_TIME = 2


class ProductApiTest(TestCase):
    client = APIClient()

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="TestCategory")
        Product.objects.bulk_create(
            [
                Product(name=f"product_{i}", price=TEST_PRODUCT_PRICE, count=TEST_PRODUCT_COUNT)
                for i in range(TEST_PRODUCT_ITEMS)
            ]
        )
        test_category.product_set.add(*Product.objects.all().values_list("id", flat=True))

    def make_request(self, url):
        t_start = timer()
        response = self.client.get(url)
        t_elapsed = timer() - t_start
        self.assertLess(t_elapsed, MAX_RESPONSE_TIME)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        return response.json()

    def test_products_list(self):
        with self.assertNumQueries(2):
            resp = self.make_request("/api/products")
        test_product = resp[0]
        self.assertEqual(len(resp), TEST_PRODUCT_ITEMS)
        self.assertIn("product_", test_product["name"])
        self.assertEqual(test_product["categories"], ["TestCategory"])
        self.assertEqual(test_product["price"], TEST_PRODUCT_PRICE)
        self.assertEqual(test_product["count"], TEST_PRODUCT_COUNT)

    def test_categories_list(self):
        resp = self.make_request("/api/categories")
        self.assertEqual(len(resp), 1)
        self.assertEqual(resp[0]["name"], "TestCategory")
