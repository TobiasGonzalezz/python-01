### Objetivo: 
- crear un logger que registre mensajes en un archivo .log, y que sea accesible desde distintos módulos o clases sin duplicarse.

### Requisitos:

- Crear una clase Logger decorada con @singleton.

- En su __init__, abrir (o crear) un archivo app.log.

- Agregar un método log(msg) que escriba mensajes con timestamps.

- Desde un segundo módulo simulado (por ejemplo otra función), usar el mismo logger y verificar que el archivo no se duplique ni cree nuevas instancias.


### 🧩 Issue #2 — “Cache global con Singleton”


### 🎯 Objetivo

Crear una clase Cache que almacene datos en memoria de forma global y única (una sola instancia compartida en toda la aplicación).
El cache debe permitir guardar, leer y eliminar valores por clave.

### 🧱 Requisitos

Usar el decorador @singleton (el mismo que ya tenés).

Crear la clase Cache con estos métodos:

set(key, value) → guarda un valor.

get(key) → devuelve el valor si existe, sino None.

delete(key) → elimina una clave del cache.

clear() → vacía completamente el cache.

Guardar los datos internamente en un diccionario (self._data).

En el constructor (__init__), inicializar el diccionario solo la primera vez.

Al crear múltiples instancias, deben compartir el mismo estado (los datos).