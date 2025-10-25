from datetime import datetime
def singleton(cls):
    instances = dict()
    
    def wrap(*args, **kwargs): 
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)    
        
        return instances[cls]

    return wrap

@singleton 
class Logger(object):
    def __init__(self, file_name="app.log"):
        self.file_name = file_name
        with open(self.file_name, "w") as f:
            f.write("Logger iniciado\n")

    def log(self, msg):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open(self.file_name, "a") as f:
            f.write(f"{timestamp} {msg}\n")

@singleton
class Cache(object):
    
    def __init__(self):
        self._data = {}
    
    def set(self, key, value):
        self._data[key] = value

    def get(self, key):
        if key in self._data:
            return self._data[key]
        else:
            return None

    def delete(self, key):
        if key in self._data:
            del self._data[key]

    def clear(self):
        self._data.clear()

if __name__ == '__main__':
    logger1 = Logger()
    msg1 = logger1.log('Hola mundo')
    msg2 = logger1.log('Corta la bocha')

    print(msg1 is msg2)

    logger2 = Logger()
    msg1 = logger2.log('Hola mundo desde 2')
    msg2 = logger2.log('Corta la bocha desde 2')

    print(msg1 is msg2)
