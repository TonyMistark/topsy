"""Test permission checker class, which is used to get user permissions on board."""

import unittest

import accounts.adapters.memory_storage as accounts_memory_storage
import notes.adapters.memory_storage as notes_memory_storage
from accounts.core.entities import User
from notes.core.entities import Board
from topsy.permissions import PermissionChecker

account_storage = accounts_memory_storage.MemoryStorage()
notes_storage = notes_memory_storage.MemoryStorage()


class PermissionCheckerTestCase(unittest.TestCase):
    def setUp(self):
        self.get_perms = PermissionChecker(notes_storage)

    def test_get_perms(self):
        """User with valid role on board should have some permissions."""
        role = "editor"
        board = notes_storage.save_board(Board(name="Fox & Raccoon"))
        user = account_storage.create_user(
            User(name="Bird", email="bird@forest.com"), "w0rm"
        )
        notes_storage.save_board_user(board.id, user.id, role)

        perms = self.get_perms(user.id, board.id)

        self.assertTrue(len(perms) > 0)

    def test_has_perm(self):
        """User with valid role on board should have some permissions."""
        role = "editor"
        board = notes_storage.save_board(Board(name="Fox & Raccoon"))
        user = account_storage.create_user(
            User(name="Bird", email="bird@forest.com"), "w0rm"
        )
        notes_storage.save_board_user(board.id, user.id, role)

        has_perm = self.get_perms(user.id, board.id, "edit_note")

        self.assertEqual(has_perm, True)

    def test_no_perms(self):
        """User without join to board should have no permissions."""
        perms = self.get_perms(10, 12)

        self.assertTrue(len(perms) == 0)
