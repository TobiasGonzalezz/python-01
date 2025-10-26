import unittest
from factory_example import FeedFactory, SoccerFeed, TennisFeed, RugbyFeed

class TestFactoryMethod(unittest.TestCase):
    def test_create_soccer_feed(self):
        data = '{"sport": "soccer"}'
        feed = FeedFactory.create_feed(data)
        self.assertIsInstance(feed, SoccerFeed)

    def test_create_tennis_feed(self):
        data = '{"sport": "tennis"}'
        feed = FeedFactory.create_feed(data)
        self.assertIsInstance(feed, TennisFeed)

    def test_unknown_feed(self):
        data = '{"sport": "basketball"}'
        with self.assertRaises(ValueError):
            FeedFactory.create_feed(data)

if __name__ == "__main__":
    unittest.main()