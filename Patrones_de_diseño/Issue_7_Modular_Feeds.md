# 🧩 Issue #7 — Modularización de Feeds con Auto-Registro y Template Method

## 🎯 Objetivo

Diseñar una arquitectura **modular, escalable y mantenible** para manejar decenas de clases de feeds (`F`, `R`, `T`, `JJOO`) distribuidas en archivos separados.  
El sistema debe seguir soportando:
- Registro dinámico (Factory Registry)
- Validación de duplicados
- Flujo estándar (Template Method)
- Auto-descubrimiento de módulos

---

## 🏗️ Contexto

Hasta ahora implementamos:
- ✅ **Factory Registry** con decoradores  
- ✅ **Validación de duplicados**  
- ✅ **Template Method** para flujos reutilizables  

Pero en tu caso real, tenés **docenas de feeds**, distribuidos en distintos archivos:
```
model_futbol.py   # Contiene F1, F2, F3...F40
model_rugby.py    # Contiene R1...R12
model_tennis.py   # Contiene T1...T20
model_jjoo.py     # Contiene JJOO1...JJOO4
```

El objetivo ahora es **unificar el flujo y hacer que todo se cargue automáticamente**, sin modificar el código central al agregar o eliminar feeds.

---

## 🧩 Estructura Propuesta

```
/project-root
│
├── feeds/
│   ├── __init__.py
│   ├── model_futbol.py
│   ├── model_rugby.py
│   ├── model_tennis.py
│   └── model_jjoo.py
│
├── factory_registry.py
├── main.py
└── Issue_7_Modular_Feeds.md
```

---

## ⚙️ Paso 1 — Base: Factory + Template Method

`factory_registry.py`
```python
import importlib, pkgutil

class FeedFactory:
    _registry = {}

    @classmethod
    def register(cls, name):
        def decorator(feed_cls):
            if name in cls._registry:
                raise ValueError(f"Feed '{name}' ya registrado con {cls._registry[name].__name__}")
            cls._registry[name] = feed_cls
            print(f"[Factory] Registrado feed '{name}' → {feed_cls.__name__}")
            return feed_cls
        return decorator

    @classmethod
    def create_feed(cls, name, data):
        feed_cls = cls._registry.get(name)
        if not feed_cls:
            raise ValueError(f"Feed '{name}' no registrado.")
        return feed_cls(data)

def auto_register_feeds(package_name="feeds"):
    # Carga dinámica de todos los feeds del paquete especificado.
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package_name}.{module_name}")


class Feed:
    # Template Method común para todos los feeds.
    def __init__(self, data):
        self.data = data

    def run(self):
        self.load()
        self.parse()
        self.save()

    def load(self):
        print("Cargando datos...")

    def parse(self):
        raise NotImplementedError

    def save(self):
        print("Guardando resultados...")
```

---

## ⚙️ Paso 2 — Feeds por tipo

### `feeds/model_futbol.py`

```python
from factory_registry import FeedFactory, Feed

@FeedFactory.register("F1")
class F1Feed(Feed):
    def parse(self):
        print("Parseando F1 (Fútbol)...")

@FeedFactory.register("F2")
class F2Feed(Feed):
    def parse(self):
        print("Parseando F2 (Fútbol)...")
```

---

### `feeds/model_rugby.py`

```python
from factory_registry import FeedFactory, Feed

@FeedFactory.register("R1")
class R1Feed(Feed):
    def parse(self):
        print("Parseando R1 (Rugby)...")
```

---

### `feeds/model_tennis.py`

```python
from factory_registry import FeedFactory, Feed

@FeedFactory.register("T1")
class T1Feed(Feed):
    def parse(self):
        print("Parseando T1 (Tennis)...")
```

---

### `feeds/model_jjoo.py`

```python
from factory_registry import FeedFactory, Feed

@FeedFactory.register("JJOO1")
class JJOO1Feed(Feed):
    def parse(self):
        print("Parseando JJOO1 (Juegos Olímpicos)...")
```

---

## ⚙️ Paso 3 — Auto-descubrimiento y ejecución

`main.py`
```python
from factory_registry import FeedFactory, auto_register_feeds

# Auto-importar todos los módulos de feeds/
auto_register_feeds()

# Crear y ejecutar feed dinámicamente
feed = FeedFactory.create_feed("F1", "<xml>...</xml>")
feed.run()
```

🔹 Salida esperada:

```
[Factory] Registrado feed 'F1' → F1Feed
[Factory] Registrado feed 'F2' → F2Feed
[Factory] Registrado feed 'R1' → R1Feed
[Factory] Registrado feed 'T1' → T1Feed
[Factory] Registrado feed 'JJOO1' → JJOO1Feed

Cargando datos...
Parseando F1 (Fútbol)...
Guardando resultados...
```

---

## 🧪 Tests sugeridos

### `test_auto_registration.py`

```python
import unittest
from factory_registry import FeedFactory, auto_register_feeds

class TestAutoRegistration(unittest.TestCase):
    def test_feeds_are_loaded(self):
        auto_register_feeds()
        self.assertIn("F1", FeedFactory._registry)
        self.assertIn("R1", FeedFactory._registry)
        self.assertIn("T1", FeedFactory._registry)
        self.assertIn("JJOO1", FeedFactory._registry)
```

---

## 🚀 Ventajas de esta arquitectura

| Concepto | Beneficio |
|-----------|------------|
| **Auto-descubrimiento de feeds** | Carga automática desde `/feeds` |
| **Template Method** | Flujo estandarizado (load → parse → save) |
| **Factory Registry** | Registro dinámico sin `if` ni imports manuales |
| **Validación de duplicados** | Evita conflictos entre modelos |
| **Modularidad** | Cada tipo de feed tiene su propio archivo |
| **Escalabilidad** | Podés tener 100+ feeds sin tocar el core |

---

## 🔧 Siguientes mejoras opcionales

1. **Agregar metadatos al registro** (tipo, versión, categoría, país, etc.).
2. **Incluir logging estructurado (con `logging` o AWS CloudWatch)**.
3. **Permitir dependencias entre feeds (ej. `F20` depende de `F1`)**.
4. **Convertirlo en un sistema de plugins externo (con `entry_points`)**.
5. **Soporte de configuración JSON/YAML para definir el flujo de ejecución.**

---

## 💡 Conclusión

Este patrón de modularización logra:

- Separar la lógica de negocio por deporte o categoría.
- Centralizar el registro y la ejecución.
- Mantener un flujo de procesamiento estándar.
- Escalar sin tocar el core (`factory_registry.py`).

Esta es la arquitectura base ideal para proyectos de **ingestión de datos, parsers masivos, ETL o pipelines serverless** en AWS o cualquier backend moderno.

---

> 🚀 **Próximo paso sugerido:**  
> Extender esta arquitectura con un sistema de **metadata y configuración externa (JSON/YAML)** para que los feeds puedan autodescribirse y ser activados dinámicamente según reglas o entornos.
