class Feed:

    def __init__(self, data):
        self.data = data

    def parse(self):
        raise NotImplementedError

    def get_summary(self):
        raise NotImplementedError

class FeedFactory:
    @staticmethod
    def create_feed(data):
        if '"sport": "soccer"' in data:
            return SoccerFeed(data)
        elif '"sport": "tennis"' in data:
            return TennisFeed(data)
        elif '"sport": "rugby"' in data:
            return RugbyFeed(data)
        else:
            raise ValueError("Tipo de feed desconocido")



class SoccerFeed(Feed):
    def parse(self):
        print("Procesando feed de Fútbol...")

    def get_summary(self):
        return "Resumen: Partido entre equipos A y B."


class TennisFeed(Feed):
    def parse(self):
        print("Procesando feed de Tenis...")

    def get_summary(self):
        return "Resumen: Partido entre dos jugadores de tenis."


class RugbyFeed(Feed):
    def parse(self):
        print("Procesando feed de Rugby...")

    def get_summary(self):
        return "Resumen: Partido de rugby en progreso."


if __name__ == "__main__":
       raw_data = '{"sport": "rugby", "teams": ["A", "B"]}'
       feed = FeedFactory.create_feed(raw_data)
       feed.parse()
       print(feed.get_summary())