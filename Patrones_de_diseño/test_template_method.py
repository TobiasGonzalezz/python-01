import unittest
from factory_registry_template import FeedFactory, Feed

class TestTemplateMethod(unittest.TestCase):
    def test_feed_run_flow(self):
        @FeedFactory.register("demo")
        class DemoFeed(Feed):
            def parse(self):
                self.executed = True

        feed = FeedFactory.create_feed("demo", "<xml>...</xml>")
        feed.run()
        self.assertTrue(hasattr(feed, "executed"))