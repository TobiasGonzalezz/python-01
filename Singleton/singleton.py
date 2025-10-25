def singleton(cls): # Decorador para clases
    # Metodo "pythonica"
    instances = dict()
    
    def wrap(*args, **kwargs): # *args listado de argunmentos y **kwargs dicionario de argumentos
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)    
        
        return instances[cls]

    return wrap

@singleton # decoramos la clase
class User(object):
    
    # ---------------------
    # Si quisieramos seguir con esta manera de singlethon deberiamos añadir varias validaciones lo cual lo hace poco legible, en este caso lo mejor es hacerlo de la forma "pythonica"

    # __instance = None 

    # def __new__(cls): # Un metodo estatico por ende no va a tener self, vaa tener cls haciendo referencia a nuestra clase
    #     if User.__instance is None: # Instanciamos un valor a nuestra instancia por unica vez
    #         print('Nueva instancia')
    #         User.__instance = object.__new__(cls)
        
    #     return User.__instance
    # ---------------------
    

    def __init__(self, username): 
        self.username = username

@singleton
class Admin():
    pass

if __name__ == '__main__':
    
    user1 = User("Cody")
    user2 = User("Tobi")

    print(user1 is user2) # recordar que con is podemos reconocer si un objeto es otro objeto.

    admin1 = Admin()
    admin2 = Admin()

    print(admin1 is admin2)