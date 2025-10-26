# 🧩 Issue #5 — Implementar una Factory con Registro Dinámico (Auto-registro con Decoradores)

## 🎯 Objetivo

Aprender a construir una **fábrica extensible** donde las clases se **auto-registran** al definirse, eliminando los `if/elif` y mejorando la mantenibilidad.  
Este patrón es una evolución directa del **Factory Method** hacia un **Factory Registry Pattern** con decoradores.

---

## 🏗️ Contexto

En proyectos grandes (como tu sistema con múltiples clases `F1`, `F3`, `F9`, etc.), mantener una fábrica con condicionales es costoso y propenso a errores.

Este ejercicio propone reemplazar esa estructura con un **registro centralizado** donde cada clase se “anota” automáticamente al definirse.  
Así, agregar un nuevo tipo solo requiere crear la clase y aplicar el decorador.

---

## 🧠 Requisitos

1. Crear una clase base `Feed` con un constructor común:

   ```python
   class Feed:
       def __init__(self, data):
           self.data = data

       def parse(self):
           raise NotImplementedError
   ```

2. Crear la **fábrica dinámica** `FeedFactory`:

   ```python
   class FeedFactory:
       _registry = {}

       @classmethod
       def register(cls, name):
           def decorator(feed_cls):
               cls._registry[name] = feed_cls
               return feed_cls
           return decorator

       @classmethod
       def create_feed(cls, name, data):
           feed_cls = cls._registry.get(name)
           if not feed_cls:
               raise ValueError(f"Feed '{name}' no registrado")
           return feed_cls(data)
   ```

   🔸 `register()` es un **decorador de clase** que agrega el tipo al registro global.  
   🔸 `create_feed()` crea dinámicamente la instancia correcta.

3. Crear tres feeds concretos:

   ```python
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
   ```

4. Probar el flujo:

   ```python
   if __name__ == "__main__":
       feed = FeedFactory.create_feed("soccer", "<xml>...</xml>")
       feed.parse()
   ```

---

## ✅ Resultado Esperado

Al ejecutar el script:

```
Procesando feed de Fútbol...
```

Y si llamás:

```python
FeedFactory.create_feed("rugby", "<xml>...</xml>")
```
Obtendrás:
```
Procesando feed de Rugby...
```

---

## 🧪 Test Sugerido — `test_factory_registry.py`

```python
import unittest
from factory_registry import FeedFactory, SoccerFeed, TennisFeed, RugbyFeed

class TestFactoryRegistry(unittest.TestCase):
    def test_feed_registration(self):
        self.assertIn("soccer", FeedFactory._registry)
        self.assertIn("tennis", FeedFactory._registry)
        self.assertIn("rugby", FeedFactory._registry)

    def test_feed_creation(self):
        soccer = FeedFactory.create_feed("soccer", "data")
        tennis = FeedFactory.create_feed("tennis", "data")
        rugby = FeedFactory.create_feed("rugby", "data")

        self.assertIsInstance(soccer, SoccerFeed)
        self.assertIsInstance(tennis, TennisFeed)
        self.assertIsInstance(rugby, RugbyFeed)

    def test_invalid_feed(self):
        with self.assertRaises(ValueError):
            FeedFactory.create_feed("basketball", "data")

if __name__ == "__main__":
    unittest.main()
```

---

## ⚙️ Ventajas Clave del Patrón de Registro Dinámico

| Problema anterior | Solución con registro |
|--------------------|----------------------|
| `if/elif` interminables en la fábrica | Las clases se auto-registran |
| Modificar la fábrica en cada nuevo tipo | No se toca la fábrica |
| Riesgo de typos o duplicaciones | Registro central validado |
| Dificultad para testear o extender | Agregás tipos sin romper código existente |

---

## 🚀 Siguientes Pasos (para profundizar)

### 🧩 Paso 1 — Agregar *auto-descubrimiento de módulos*
Hacer que el sistema importe automáticamente todas las clases `Feed` desde una carpeta `/feeds` al iniciar.  
Esto permite que el registro se llene solo.

### 🧩 Paso 2 — Combinar con **Template Method**
Definir en `Feed` pasos comunes (parsear, validar, guardar) y dejar a las subclases los pasos específicos.

### 🧩 Paso 3 — Integrar con **Chain of Responsibility**
Si hay condiciones complejas (por contenido del XML, no solo el nombre), los `FeedHandlers` pueden decidir si procesar o pasar el control al siguiente.

---

## 🧱 Estructura de Archivos Sugerida

```
/project-root
│
├── factory_registry.py         # Implementación del patrón
├── test_factory_registry.py    # Tests unitarios
└── Issue_5_Factory_Registry.md # Este documento
```

---

## 💡 Conclusión

Este patrón te enseña cómo:
- Crear **fábricas inteligentes** que se auto-extienden.  
- Aplicar decoradores como mecanismo de **auto-registro dinámico**.  
- Escalar un sistema con decenas de clases (`F1`, `F3`, `F9`, etc.) sin modificar el núcleo.

Es una práctica fundamental para arquitecturas de **plugins**, **handlers** o **parsers** distribuidos en proyectos grandes (por ejemplo, AWS Lambda, Django, FastAPI, o frameworks de ETL).

---

> 🚀 **Próximo paso sugerido:**  
> Migrar este patrón hacia una versión con *auto-descubrimiento de módulos*, donde la fábrica detecte automáticamente todos los feeds al importar el paquete.
