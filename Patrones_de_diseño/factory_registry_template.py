class Feed:
    "Clase base con flujo estándar."
    def __init__(self, data):
        self.data = data

    def run(self):
        "Template Method: define el flujo común."
        self.load()
        self.parse()
        self.save()

    def load(self):
        print("Cargando datos...")

    def parse(self):
        raise NotImplementedError("Subclase debe implementar 'parse'")

    def save(self):
        print("Guardando resultados...")

class FeedFactory:
    _registry = {}

    @classmethod
    def register(cls, name):
        def decorator(feed_cls):
            if name in cls._registry:
                raise ValueError(f"❌ Feed '{name}' ya está registrado con {cls._registry[name].__name__}")
            cls._registry[name] = feed_cls
            print(f"[Factory] ✅ Registrado feed '{name}' → {feed_cls.__name__}")
            return feed_cls
        return decorator

    @classmethod
    def create_feed(cls, name, data):
        feed_cls = cls._registry.get(name)
        if not feed_cls:
            raise ValueError(f"⚠️ Feed '{name}' no registrado.")
        return feed_cls(data)
    
@FeedFactory.register("F1")
class F1Feed(Feed):
    def parse(self):
        print("Procesando feed F1...")

@FeedFactory.register("F2")
class F2Feed(Feed):
    def parse(self):
        print("Procesando feed F2...")

@FeedFactory.register("F9")
class F9Feed(Feed):
    def parse(self):
        print("Procesando feed F9...")
    
    def load(self):
        print('Nuevo metodo')

if __name__ == "__main__":
    feed = FeedFactory.create_feed("F9", "<xml>...</xml>")
    feed.run()