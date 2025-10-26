import unittest
from factory_registry import FeedFactory, SoccerFeed, TennisFeed, RugbyFeed

class TestFactoryRegistry(unittest.TestCase):
    def test_feed_registration(self):
        self.assertIn("soccer", FeedFactory._registry)
        self.assertIn("tennis", FeedFactory._registry)
        self.assertIn("rugby", FeedFactory._registry)

    def test_feed_creation(self):
        soccer = FeedFactory.create_feed("soccer", "data")
        tennis = FeedFactory.create_feed("tennis", "data")
        rugby = FeedFactory.create_feed("rugby", "data")

        self.assertIsInstance(soccer, SoccerFeed)
        self.assertIsInstance(tennis, TennisFeed)
        self.assertIsInstance(rugby, RugbyFeed)

    def test_invalid_feed(self):
        with self.assertRaises(ValueError):
            FeedFactory.create_feed("basketball", "data")

if __name__ == "__main__":
    unittest.main()