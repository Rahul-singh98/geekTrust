from unittest import TestCase, main
from src import products_builder
from src import products


class TestBuilder(TestCase):
    def test_get_product(self):
        builder = products_builder.Builder()
        tshirt_object = builder.get_product("TShirt")
        self.assertIsInstance(
            tshirt_object,
            products.TShirt
        )

if __name__ == "__main__":
    main()