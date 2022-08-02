from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('Test_store')
        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        with self.app_context():
            store = StoreModel('Test_store')
            self.assertIsNone(store.find_by_name('Test_store'))
            store.save_to_db()
            self.assertIsNotNone(store.find_by_name('Test_store'))
            store.delete_from_db()
            self.assertIsNone(store.find_by_name('Test_store'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test_store')
            item = ItemModel('Test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'Test')
            self.assertEqual(store.items.first().price, 19.99)
            self.assertEqual(store.items.first().store_id, 1)

    def test_store_json(self):
        store = StoreModel('Test_store')
        expected_json = {
            'name': 'Test_store',
            'items': []
        }

        self.assertDictEqual(store.json(), expected_json)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('Test_store')
            item = ItemModel('Test', 19.99, 1)
            store.save_to_db()
            item.save_to_db()
            expected_json = {
                'name': 'Test_store',
                'items': [{'name': 'Test', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected_json)