"""Adapter for Django ORM.

Pretty much all calls to the database in the live app should go through the methods of this class.
The MemoryStorage class shares the same interface, but doesn't depend on an actual database. It can
be swapped out for this one when testing use cases.
"""
