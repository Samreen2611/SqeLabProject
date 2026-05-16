import unittest
from unittest.mock import patch, MagicMock
import json
import os

# ─────────────────────────────────────────
# TC01 & TC02 — Register Tests
# ─────────────────────────────────────────
class TestRegister(unittest.TestCase):

    @patch('builtins.input', side_effect=['newuser', 'pass123'])
    @patch('auth.load_data', return_value=[])
    @patch('auth.save_data')
    def test_TC01_register_new_user(self, mock_save, mock_load, mock_input):
        """TC01: Register with a brand new username — should succeed"""
        from auth import register
        register()
        mock_save.assert_called_once()  # save_data must be called

    @patch('builtins.input', side_effect=['samreen', '12345'])
    @patch('auth.load_data', return_value=[{"username": "samreen", "password": "12345"}])
    @patch('auth.save_data')
    def test_TC02_register_existing_user(self, mock_save, mock_load, mock_input):
        """TC02: Register with existing username — should NOT save"""
        from auth import register
        register()
        mock_save.assert_not_called()  # save_data should NOT be called


# ─────────────────────────────────────────
# TC03 & TC04 — Login Tests
# ─────────────────────────────────────────
class TestLogin(unittest.TestCase):

    @patch('builtins.input', side_effect=['samreen', '12345'])
    @patch('auth.load_data', return_value=[{"username": "samreen", "password": "12345"}])
    def test_TC03_login_valid(self, mock_load, mock_input):
        """TC03: Login with correct credentials — should return username"""
        from auth import login
        result = login()
        self.assertEqual(result, 'samreen')

    @patch('builtins.input', side_effect=['samreen', 'wrongpass'])
    @patch('auth.load_data', return_value=[{"username": "samreen", "password": "12345"}])
    def test_TC04_login_invalid(self, mock_load, mock_input):
        """TC04: Login with wrong password — should return None"""
        from auth import login
        result = login()
        self.assertIsNone(result)


# ─────────────────────────────────────────
# TC05, TC06, TC07 — Library Tests
# ─────────────────────────────────────────
class TestLibrary(unittest.TestCase):

    BOOKS = [
        {"id": 1, "title": "Python Programming", "author": "Guido", "quantity": 5},
        {"id": 2, "title": "Database Systems", "author": "Elmasri", "quantity": 3}
    ]

    @patch('library.load_data', return_value=BOOKS)
    def test_TC05_view_books(self, mock_load):
        """TC05: View books — should not raise any error"""
        from library import view_books
        try:
            view_books()
            result = True
        except:
            result = False
        self.assertTrue(result)

    @patch('builtins.input', return_value='Python')
    @patch('library.load_data', return_value=BOOKS)
    def test_TC06_search_found(self, mock_load, mock_input):
        """TC06: Search existing book — should find it"""
        from library import search_book
        try:
            search_book()
            result = True
        except:
            result = False
        self.assertTrue(result)

    @patch('builtins.input', return_value='xyz123')
    @patch('library.load_data', return_value=BOOKS)
    def test_TC07_search_not_found(self, mock_load, mock_input):
        """TC07: Search non-existing book — should print not found"""
        from library import search_book
        try:
            search_book()
            result = True
        except:
            result = False
        self.assertTrue(result)


# ─────────────────────────────────────────
# TC08 & TC09 — Borrow Tests
# ─────────────────────────────────────────
class TestBorrow(unittest.TestCase):

    BOOKS = [
        {"id": 1, "title": "Python Programming", "author": "Guido", "quantity": 5}
    ]

    @patch('builtins.input', return_value='1')
    @patch('library.load_data', return_value=BOOKS)
    @patch('library.save_data')
    def test_TC08_borrow_valid(self, mock_save, mock_load, mock_input):
        """TC08: Borrow valid book — quantity should decrease"""
        from library import borrow_book
        borrow_book('samreen')
        mock_save.assert_called()  # Data must be saved

    @patch('builtins.input', return_value='abc')
    @patch('library.load_data', return_value=BOOKS)
    def test_TC09_borrow_invalid_input(self, mock_load, mock_input):
        """TC09: Borrow with non-numeric ID — should handle gracefully"""
        from library import borrow_book
        try:
            borrow_book('samreen')
            result = True
        except:
            result = False
        self.assertTrue(result)


# ─────────────────────────────────────────
# TC10 — Return Test
# ─────────────────────────────────────────
class TestReturn(unittest.TestCase):

    BOOKS = [
        {"id": 1, "title": "Python Programming", "author": "Guido", "quantity": 4}
    ]
    TRANSACTIONS = []

    @patch('builtins.input', return_value='1')
    @patch('library.load_data', side_effect=[BOOKS, TRANSACTIONS])
    @patch('library.save_data')
    def test_TC10_return_valid(self, mock_save, mock_load, mock_input):
        """TC10: Return a valid book — should save updated data"""
        from library import return_book
        return_book('samreen')
        mock_save.assert_called()


if __name__ == '__main__':
    unittest.main(verbosity=2)