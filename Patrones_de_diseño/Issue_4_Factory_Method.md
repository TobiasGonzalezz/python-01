# 🧩 Issue #4 — Implementar y Extender un Factory Method en Python

## 🎯 Objetivo

Recrear un sistema inspirado en un proyecto real (como el de feeds OPTA) que use el **patrón Factory Method** para generar objetos de diferentes tipos de datos, todos con una **interfaz común**.  
El objetivo es entender cómo delegar la **creación de instancias dinámicas** a una “fábrica” y luego extender el diseño hacia patrones más avanzados.

---

## 🏗️ Contexto

Queremos simular un **procesador de feeds deportivos**, que recibe datos en formato JSON y crea un objeto especializado según el tipo detectado.  
Cada tipo de feed (fútbol, tenis, rugby) se comporta distinto, pero comparten la misma estructura base.

---

## 🧠 Requisitos

1. Crear una clase base `Feed` con una interfaz común:

   ```python
   class Feed:
       def parse(self):
           raise NotImplementedError

       def get_summary(self):
           raise NotImplementedError
   ```

2. Crear tres subclases:
   - `SoccerFeed`
   - `TennisFeed`
   - `RugbyFeed`

   Cada una debe implementar `parse()` y `get_summary()` con su propio comportamiento.

3. Crear una **fábrica** llamada `FeedFactory` con un método estático:

   ```python
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
   ```

4. Crear un script principal que use la fábrica:

   ```python
   if __name__ == "__main__":
       raw_data = '{"sport": "soccer", "teams": ["A", "B"]}'
       feed = FeedFactory.create_feed(raw_data)
       feed.parse()
       print(feed.get_summary())
   ```

---

## ✅ Resultado Esperado

Al ejecutar el script debería imprimirse:

```
Procesando feed de Fútbol...
Resumen: Partido entre equipos A y B.
```

Si cambiás el tipo de deporte (`tennis`, `rugby`), el comportamiento cambia dinámicamente.

---

## 🧪 Test Sugerido — `test_factory_method.py`

```python
import unittest
from factory_example import FeedFactory, SoccerFeed, TennisFeed, RugbyFeed

class TestFactoryMethod(unittest.TestCase):
    def test_create_soccer_feed(self):
        data = '{"sport": "soccer"}'
        feed = FeedFactory.create_feed(data)
        self.assertIsInstance(feed, SoccerFeed)

    def test_create_tennis_feed(self):
        data = '{"sport": "tennis"}'
        feed = FeedFactory.create_feed(data)
        self.assertIsInstance(feed, TennisFeed)

    def test_unknown_feed(self):
        data = '{"sport": "basketball"}'
        with self.assertRaises(ValueError):
            FeedFactory.create_feed(data)

if __name__ == "__main__":
    unittest.main()
```

---

## 🔁 Siguientes Pasos de Evolución

### 🧩 **Paso 1: Abstract Factory**

Crea una fábrica distinta por deporte:

```python
class SoccerFactory:
    def create(self, data):
        return SoccerFeed(data)
```

Y una clase que decida cuál usar:

```python
class FeedFactoryProvider:
    def get_factory(self, sport):
        if sport == "soccer":
            return SoccerFactory()
        # otros casos...
```

**Ventaja:** separación por dominio y escalabilidad modular.

---

### ⚙️ **Paso 2: Chain of Responsibility**

Reemplazá los `if` por una cadena de manejadores:

```python
class FeedHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, data):
        if '"sport": "soccer"' in data:
            return SoccerFeed(data)
        elif self.next_handler:
            return self.next_handler.handle(data)
```

**Ventaja:** se agregan nuevos tipos sin modificar código existente.

---

### 🎨 **Paso 3: Template Method**

Centralizá la estructura común en la clase base:

```python
class Feed:
    def parse(self):
        print(f"Procesando feed de {self.get_sport_name()}")

    def get_summary(self):
        raise NotImplementedError
```

**Ventaja:** evita duplicación y asegura consistencia entre clases hijas.

---

### 🧩 **Paso 4: Strategy Pattern**

Separá la lógica de guardado o procesamiento:

```python
class SaveToS3:
    def execute(self, feed):
        print("Guardando en S3...")

class SaveToLocal:
    def execute(self, feed):
        print("Guardando localmente...")
```

**Ventaja:** permite cambiar el comportamiento sin modificar la lógica principal  
(ideal para entornos serverless o microservicios).

---

## ⚙️ Tabla Comparativa de Ventajas

| Nivel | Patrón | Qué mejora | Ventaja principal |
|-------|---------|-------------|-------------------|
| 1 | Factory Method | Creación de objetos | Flexibilidad y desacoplamiento |
| 2 | Abstract Factory | Agrupación por dominio | Escalabilidad modular |
| 3 | Chain of Responsibility | Flujo extensible | Eliminación de `if` anidados |
| 4 | Template Method | Reutilización estructural | Consistencia y DRY |
| 5 | Strategy | Comportamiento configurable | Alta flexibilidad sin acoplar código |

---

## 🧱 Estructura de Archivos Sugerida

```
/project-root
│
├── factory_example.py        # Implementación principal del patrón Factory
├── test_factory_method.py    # Tests unitarios
└── Issue_4_Factory_Method.md # Este documento
```

---

## 💡 Conclusión

Este ejercicio te enseña cómo:
- Centralizar la creación de objetos de distintos tipos.
- Extender el sistema sin tocar el código base.
- Evolucionar hacia patrones más sofisticados que mejoran mantenibilidad y escalabilidad.

El patrón **Factory Method** es ampliamente usado en proyectos con frameworks como Django, Flask o FastAPI, donde la creación de instancias dinámicas (según tipo, endpoint o modelo) es constante.

---

> 🚀 **Próximo paso sugerido:**  
> Migrar este diseño hacia una versión con **Chain of Responsibility**, donde cada handler se encargue de detectar y procesar su tipo de feed, eliminando por completo los `if` de la fábrica.
