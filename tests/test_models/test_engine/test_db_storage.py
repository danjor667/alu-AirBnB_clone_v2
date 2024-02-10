#!/usr/bin/python3
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not fs")
class TestDBStorage(unittest.TestCase):
    """DB Storage test"""

    def setUp(self):
        """ Set up test environment """
        self.storage = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.storage

    def test_user(self):
        """ Tests user """
        user = User(name="John", email="John@gmail.com", password="John12345")
        user.save()
        self.assertFalse(user.id in self.storage.all())
        self.assertEqual(user.name, "John")

    def test_city(self):
        """ test city """
        state = State(name="California")
        state.save()
        city = City(name="Fresno")
        city.state_id = state.id
        city.save()
        self.assertFalse(city.id in self.storage.all())
        self.assertEqual(city.name, "Fresno")

    def test_state(self):
        """ test state"""
        state = State(name="California")
        state.save()
        self.assertFalse(state.id in self.storage.all())
        self.assertEqual(state.name, "California")

    def test_place(self):
        """Test place"""
        state = State(name="California")
        state.save()

        city = City(name="Fresno")
        city.state_id = state.id
        city.save()

        user = User(name="John", email="John@gmail.com", password="John12345")
        user.save()

        place = Place(name="home", number_rooms=4)
        place.city_id = city.id
        place.user_id = user.id
        place.save()

        self.assertFalse(place.id in self.storage.all())
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.name, "home")

    def test_amenity(self):
        """ test amenity """
        amenity = Amenity(id="test1_id", name="Starlink")
        amenity.save()
        self.assertFalse(amenity.name, None)
        self.assertTrue(amenity.name, "Starlink")

    def test_review(self):
        """ test review """
        state = State(name="California")
        state.save()

        city = City(name="Fresno")
        city.state_id = state.id
        city.save()

        user = User(name="John", email="John@gmail.com", password="John12345")
        user.save()

        place = Place(name="home", number_rooms=4)
        place.city_id = city.id
        place.user_id = user.id
        place.save()

        review = Review(text="no comment", place_id=place.id, user_id=user.id)
        review.save()

        self.assertFalse(review.id in self.storage.all())
        self.assertEqual(review.text, "no comment")


if __name__ == '__main__':
    unittest.main()