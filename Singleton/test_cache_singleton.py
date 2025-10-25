import unittest
from logger_singleton import Cache, singleton

class TestCacheSingleton(unittest.TestCase):

    def setUp(self):
        # Reiniciar el cache del decorador entre tests
        singleton.instances = {}

    def test_singleton_instance(self):
        c1 = Cache()
        c2 = Cache()
        self.assertIs(c1, c2, "Cache no es singleton")

    def test_set_and_get(self):
        cache = Cache()
        cache.set("a", 100)
        cache.set("b", 200)
        self.assertEqual(cache.get("a"), 100)
        self.assertEqual(cache.get("b"), 200)
        self.assertIsNone(cache.get("x"))  # clave inexistente

    def test_shared_state(self):
        c1 = Cache()
        c2 = Cache()
        c1.set("user", "Cody")
        self.assertEqual(c2.get("user"), "Cody")  # misma instancia

    def test_delete_and_clear(self):
        cache = Cache()
        cache.set("temp", 123)
        cache.delete("temp")
        self.assertIsNone(cache.get("temp"))

        cache.set("a", 1)
        cache.set("b", 2)
        cache.clear()
        self.assertEqual(len(cache._data), 0)

if __name__ == "__main__":
    unittest.main()
