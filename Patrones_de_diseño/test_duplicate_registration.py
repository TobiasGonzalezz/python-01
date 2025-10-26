import unittest
from factory_registry_template import FeedFactory

class TestDuplicateRegistration(unittest.TestCase):
    def test_duplicate_registration_raises(self):
        @FeedFactory.register("soccer")
        class SoccerFeed:
            pass

        with self.assertRaises(ValueError):
            @FeedFactory.register("soccer")
            class SoccerFeedDuplicate:
                pass