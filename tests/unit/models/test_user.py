from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('Test', 'Test_password')
        self.assertEqual(user.username, 'Test')
        self.assertEqual(user.password, 'Test_password')

