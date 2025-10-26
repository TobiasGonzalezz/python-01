class Feed:
    def __init__(self, data):
        self.data = data

    def parse(self):
        raise NotImplementedError

class FeedFactory:
    _registry = {}

    @classmethod
    def register(cls, name): # es un **decorador de clase** que agrega el tipo al registro global
        def decorator(feed_cls):
            cls._registry[name] = feed_cls
            return feed_cls
        return decorator

    @classmethod
    def create_feed(cls, name, data): # crea dinámicamente la instancia correcta.
        feed_cls = cls._registry.get(name)
        if not feed_cls:
            raise ValueError(f"Feed '{name}' no registrado")
        return feed_cls(data)
    
@FeedFactory.register("soccer")
class SoccerFeed(Feed):
    def parse(self):
        print("Procesando feed de Fútbol...")

@FeedFactory.register("tennis")
class TennisFeed(Feed):
    def parse(self):
        print("Procesando feed de Tenis...")

@FeedFactory.register("rugby")
class RugbyFeed(Feed):
    def parse(self):
        print("Procesando feed de Rugby...")

if __name__ == "__main__":
       feed = FeedFactory.create_feed("rugby", "<xml>...</xml>")
       feed.parse()