# 🧩 Issue #6 — Template Method + Validación de Duplicados en Factory Registry

## 🎯 Objetivo

Aprender a combinar dos patrones de diseño potentes:
1. **Factory Registry con Validación de Duplicados** — para evitar errores de registro.
2. **Template Method** — para definir un flujo estándar reutilizable en todas las subclases.

---

## 🏗️ Contexto

En sistemas con múltiples clases (por ejemplo, `F1`, `F3`, `F9`), es fácil cometer errores de registro duplicado o tener comportamientos inconsistentes entre clases.  
Esta issue busca resolver ambos problemas mediante un enfoque robusto y extensible.

---

## 🧠 Requisitos

### 1. Fábrica con Validación de Duplicados

Evitar que dos clases se registren bajo el mismo nombre.  
El registro fallará con un `ValueError` si el nombre ya existe.

```python
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
```

---

### 2. Template Method — Flujo estándar para todas las subclases

Definir una clase base `Feed` con un flujo común (`run()`), y dejar que cada subclase implemente solo lo necesario.

```python
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
```

---

### 3. Implementar tres feeds concretos

```python
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
```

---

### 4. Probar el flujo

```python
if __name__ == "__main__":
    feed = FeedFactory.create_feed("F9", "<xml>...</xml>")
    feed.run()
```

🔹 Salida esperada:

```
Cargando datos...
Procesando feed F9...
Guardando resultados...
```

---

## 🧪 Tests sugeridos

### `test_duplicate_registration.py`

```python
import unittest
from factory_registry_template import FeedFactory

class TestDuplicateRegistration(unittest.TestCase):
    def test_duplicate_registration_raises(self):
        @FeedFactory.register("soccer")
        class SoccerFeed:
            pass

        with self.assertRaises(ValueError):
            @FeedFactory.register("soccer")
            class SoccerFeedDuplicate:
                pass
```

---

### `test_template_method.py`

```python
import unittest
from factory_registry_template import FeedFactory, Feed

class TestTemplateMethod(unittest.TestCase):
    def test_feed_run_flow(self):
        @FeedFactory.register("demo")
        class DemoFeed(Feed):
            def parse(self):
                self.executed = True

        feed = FeedFactory.create_feed("demo", "<xml>...</xml>")
        feed.run()
        self.assertTrue(hasattr(feed, "executed"))
```

---

## ⚙️ Ventajas combinadas

| Patrón | Beneficio |
|--------|------------|
| **Factory Registry** | Registro dinámico sin `if` ni modificaciones |
| **Validación de duplicados** | Evita errores y conflictos de nombres |
| **Template Method** | Flujo común, fácil de extender |
| **Combinación** | Arquitectura limpia, escalable y segura |

---

## 🚀 Siguientes pasos

1. **Agregar metadata en el registro** (versión, país, fuente, etc.).
2. **Integrar el Template Method con validaciones y logging**.
3. **Agregar auto–descubrimiento de módulos (`feeds/`)** para carga automática.

---

## 🧱 Estructura recomendada

```
/project-root
│
├── factory_registry_template.py              # Implementación completa
├── test_duplicate_registration.py   # Test de duplicados
├── test_template_method.py          # Test de flujo base
└── Issue_6_Template_Method.md       # Este documento
```

---

## 💡 Conclusión

Esta práctica combina **Template Method** y **Factory Registry** en un mismo sistema, lo que te permite:

- Estandarizar procesos.
- Prevenir errores de registro.
- Escalar a docenas de tipos de feed con un flujo controlado.
- Prepararte para construir arquitecturas de tipo “plugin system”.

---

> 🚀 **Próximo paso sugerido:**  
> Extender esta base con *auto-descubrimiento de clases (`feeds/`)* y *metadata en el registro*, para lograr una arquitectura de plugins totalmente modular.
